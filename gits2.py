import argparse
import subprocess
import json
import os

base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "shortcuts.json"), "r") as f:
    data = json.load(f)

def run_dynamic_shortcut(args):
    for shortcut in data["shortcuts"]:
        if shortcut["name"].lower() == args.func_name.lower():
            for cmd in shortcut["run"]:
                cmd = cmd.replace("${text}", getattr(args, "text", ""))
                subprocess.run(cmd, shell=True)
            break
    else:
        print(f"Shortcut '{args.func_name}' bulunamadı.")

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

def main():
    parser = argparse.ArgumentParser(prog="gits", description="Benim özel CLI'm")
    subparsers = parser.add_subparsers(title="Komutlar")

    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("-m", "--message")
    commit_parser.add_argument("branch", nargs="?", default="")
    commit_parser.set_defaults(func=commit)

    repo_parser = subparsers.add_parser("repo")
    repo_parser.add_argument("url")
    repo_parser.set_defaults(func=repo)

    for shortcut in data["shortcuts"]:
        sc_parser = subparsers.add_parser(shortcut["name"])
        sc_parser.add_argument("--text", help="Shortcut içindeki ${text} yerine geçecek değer", default="")
        sc_parser.set_defaults(func=run_dynamic_shortcut, func_name=shortcut["name"])

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
