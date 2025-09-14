import argparse
import subprocess
import json
import os

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, "shortcuts.json")

def ensure_json_file():
    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump({"shortcuts": []}, f, ensure_ascii=False, indent=4)

def load_data():
    ensure_json_file()
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def run_dynamic_shortcut(args, data):
    target = None
    for shortcut in data["shortcuts"]:
        if shortcut["name"].lower() == args.func_name.lower():
            target = shortcut
            break

    if not target:
        print(f"Shortcut '{args.func_name}' bulunamadı.")
        return

    values = {}
    for var in target.get("args", []):
        values[var] = getattr(args, var, "")

    missing = [v for v in target.get("args", []) if not values.get(v)]
    if missing:
        print(f"Eksik argüman(lar): {', '.join(missing)}")
        return

    for cmd in target.get("run", []):
        filled = cmd
        for var_name, var_value in values.items():
            filled = filled.replace(f"${{{var_name}}}", str(var_value))
        subprocess.run(filled, shell=True)

def commit(args):
    subprocess.run(["git", "add", "."])
    message = args.message if args.message else "Auto commit"
    try:
        subprocess.run(["git", "commit", "-m", message], check=True)
    except subprocess.CalledProcessError:
        print("Commit edilecek değişiklik yok.")
        return
    if args.branch:
        subprocess.run(["git", "push", "-u", "origin", args.branch])
    else:
        subprocess.run(["git", "push"])

def repo(args):
    subprocess.run('echo "# New Repository" > README.md', shell=True)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "first commit"])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin", args.url])
    subprocess.run(["git", "push", "-u", "origin", "main"])

def create(args):
    data = load_data()
    name = args.name

    try:
        variables = json.loads(args.variables)
        if not isinstance(variables, list) or not all(isinstance(x, str) for x in variables):
            print("Değişkenler bir string listesi olmalı. Örn: '[\"deg1\",\"deg2\"]'")
            return
    except json.JSONDecodeError:
        print("Değişken listesi JSON formatında olmalı. Örn: '[\"deg1\",\"deg2\"]'")
        return

    commands = args.commands
    for i in range(len(commands)):
        for var in variables:
            commands[i] = commands[i].replace(f"${var}", f"${{{var}}}")

    for sc in data["shortcuts"]:
        if sc["name"].lower() == name.lower():
            print(f"'{name}' adlı bir shortcut zaten var.")
            return

    new_shortcut = {
        "name": name,
        "args": variables,
        "run": commands
    }
    data["shortcuts"].append(new_shortcut)
    save_data(data)

    print(f"Shortcut '{name}' eklendi.")
    if variables:
        print(f"Kullanım: gits {name} " + " ".join(f"<{v}>" for v in variables))
    else:
        print(f"Kullanım: gits {name}")

def delete(args):
    data = load_data()
    name = args.name

    original_len = len(data["shortcuts"])
    data["shortcuts"] = [sc for sc in data["shortcuts"] if sc["name"].lower() != name.lower()]

    if len(data["shortcuts"]) == original_len:
        print(f"'{name}' adlı bir shortcut bulunamadı.")
    else:
        save_data(data)
        print(f"Shortcut '{name}' silindi.")

def build_parser_with_dynamic_subcommands():
    data = load_data()

    parser = argparse.ArgumentParser(prog="gits")
    subparsers = parser.add_subparsers()

    commit_parser = subparsers.add_parser("commit", help="Git commit + push")
    commit_parser.add_argument("-m", "--message", help="Commit mesajı / Commit message")
    commit_parser.add_argument("branch", nargs="?", default="", help="Push yapılacak branch (opsiyonel) / Optional branch to push")
    commit_parser.set_defaults(func=commit, _type="static")

    repo_parser = subparsers.add_parser("repo", help="Yeni repo hazırla ve push et / Create new repo and push")
    repo_parser.add_argument("url", help="Remote origin URL")
    repo_parser.set_defaults(func=repo, _type="static")

    create_parser = subparsers.add_parser("create", help="Yeni shortcut oluştur / Create new shortcut")
    create_parser.add_argument("name", help="Shortcut ismi / Shortcut name")
    create_parser.add_argument("variables", help="JSON formatında değişken listesi / JSON list of variables")
    create_parser.add_argument("commands", nargs="+", help="Çalıştırılacak komutlar / Commands to run")
    create_parser.set_defaults(func=create, _type="static")

    delete_parser = subparsers.add_parser("delete", help="Shortcut sil / Delete shortcut")
    delete_parser.add_argument("name", help="Silinecek shortcut ismi / Shortcut name to delete")
    delete_parser.set_defaults(func=delete, _type="static")

    for shortcut in data.get("shortcuts", []):
        sc_parser = subparsers.add_parser(shortcut["name"], help=f"Shortcut: {shortcut['name']}")
        for var in shortcut.get("args", []):
            sc_parser.add_argument(var)
        sc_parser.set_defaults(func=run_dynamic_shortcut, func_name=shortcut["name"], _type="dynamic", _data=data)

    return parser

def main():
    parser = build_parser_with_dynamic_subcommands()
    args = parser.parse_args()

    if hasattr(args, "func"):
        if getattr(args, "_type", "") == "dynamic":
            args.func(args, args._data)
        else:
            args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
