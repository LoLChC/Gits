#!/usr/bin/env python3
import argparse
import subprocess
import json
import os
import sys
from typing import Dict, List, Any

# KURULUM DİZİNİ DEĞİŞTİ - /opt/gits olarak ayarlandı
BASE_DIR = "/opt/gits"
JSON_PATH = os.path.join(BASE_DIR, "shortcuts.json")

def ensure_json_file():
    """Ensure the shortcuts JSON file exists"""
    try:
        # Önce dizinin var olduğundan emin ol
        os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
        
        if not os.path.exists(JSON_PATH):
            with open(JSON_PATH, "w", encoding="utf-8") as f:
                json.dump({"shortcuts": []}, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"JSON dosyası oluşturulurken hata: {e}")
        # Ev dizininde yedek oluştur
        home_dir = os.path.expanduser("~")
        fallback_path = os.path.join(home_dir, ".gits_shortcuts.json")
        print(f"Yedek dosya oluşturuluyor: {fallback_path}")
        
        with open(fallback_path, "w", encoding="utf-8") as f:
            json.dump({"shortcuts": []}, f, ensure_ascii=False, indent=4)
        
        return fallback_path
    return JSON_PATH

def load_data() -> Dict[str, Any]:
    """Load shortcuts data from JSON file"""
    json_path = ensure_json_file()
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Boş bir veri yapısı döndür
        return {"shortcuts": []}

def save_data(data: Dict[str, Any]):
    """Save shortcuts data to JSON file"""
    try:
        json_path = ensure_json_file()
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Veri kaydedilirken hata: {e}")

def run_dynamic_shortcut(args, data):
    """Execute a dynamic shortcut with provided arguments"""
    target = None
    for shortcut in data["shortcuts"]:
        if shortcut["name"].lower() == args.func_name.lower():
            target = shortcut
            break

    if not target:
        print(f"Shortcut '{args.func_name}' not found.")
        return

    # Collect values for all variables
    values = {}
    for var in target.get("args", []):
        values[var] = getattr(args, var, "")

    # Check for missing required arguments
    missing = [v for v in target.get("args", []) if not values.get(v)]
    if missing:
        print(f"Missing argument(s): {', '.join(missing)}")
        return

    # Execute each command in the shortcut
    for cmd in target.get("run", []):
        filled_cmd = cmd
        for var_name, var_value in values.items():
            filled_cmd = filled_cmd.replace(f"${{{var_name}}}", str(var_value))
            filled_cmd = filled_cmd.replace(f"{{{var_name}}}", str(var_value))
        
        # Executing mesajını KALDIRDIM - sadece komutu çalıştır
        try:
            subprocess.run(filled_cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            break

def commit(args):
    """Git commit and push functionality"""
    try:
        subprocess.run(["git", "add", "."], check=True)
        message = args.message if args.message else "Auto commit"
        subprocess.run(["git", "commit", "-m", message], check=True)
        
        if args.branch:
            subprocess.run(["git", "push", "-u", "origin", args.branch], check=True)
        else:
            subprocess.run(["git", "push"], check=True)
            
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")

def repo(args):
    """Initialize and push to a new repository"""
    try:
        subprocess.run('echo "# New Repository" > README.md', shell=True, check=True)
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "first commit"], check=True)
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        subprocess.run(["git", "remote", "add", "origin", args.url], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Repository setup failed: {e}")

def create(args):
    """Create a new shortcut"""
    data = load_data()
    name = args.name

    # Değişkenleri parse et
    variables_input = args.variables
    
    # Basit liste formatını kullan
    variables = [v.strip() for v in variables_input.split(',') if v.strip()]

    if not variables:
        print("No variables found. Use: 'var1,var2' format")
        return

    # Komutları işle
    processed_commands = []
    for cmd in args.commands:
        # Komuttaki değişken referanslarını düzelt
        fixed_cmd = cmd
        for var in variables:
            # Tüm değişken formatlarını standart {var} formatına çevir
            fixed_cmd = fixed_cmd.replace(f'${{{var}}}', f'{{{var}}}')
            fixed_cmd = fixed_cmd.replace(f'${var}', f'{{{var}}}')
        processed_commands.append(fixed_cmd)

    # Kısayol zaten var mı kontrol et
    for sc in data["shortcuts"]:
        if sc["name"].lower() == name.lower():
            print(f"Shortcut '{name}' already exists.")
            return

    # Yeni kısayol ekle
    new_shortcut = {
        "name": name,
        "args": variables,
        "run": processed_commands
    }
    data["shortcuts"].append(new_shortcut)
    save_data(data)

    print(f"Shortcut '{name}' added.")
    if variables:
        print(f"Usage: gits {name} " + " ".join(f"<{v}>" for v in variables))
    else:
        print(f"Usage: gits {name}")

def delete(args):
    """Delete a shortcut"""
    data = load_data()
    name = args.name

    original_count = len(data["shortcuts"])
    data["shortcuts"] = [sc for sc in data["shortcuts"] if sc["name"].lower() != name.lower()]

    if len(data["shortcuts"]) == original_count:
        print(f"Shortcut '{name}' not found.")
    else:
        save_data(data)
        print(f"Shortcut '{name}' deleted.")

def list_shortcuts(args):
    """List all available shortcuts"""
    data = load_data()
    if not data["shortcuts"]:
        print("No shortcuts available.")
        return
    
    print("Available shortcuts:")
    for i, shortcut in enumerate(data["shortcuts"], 1):
        variables = shortcut.get("args", [])
        print(f"{i}. {shortcut['name']}")
        if variables:
            print(f"   Variables: {', '.join(variables)}")
        if "run" in shortcut:
            for j, cmd in enumerate(shortcut['run'], 1):
                print(f"   Command {j}: {cmd}")
        print()

def build_parser_with_dynamic_subcommands():
    """Build CLI parser with dynamic subcommands from shortcuts"""
    data = load_data()

    parser = argparse.ArgumentParser(prog="gits", description="Git Shortcuts Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Commit command
    commit_parser = subparsers.add_parser("commit", help="Git commit + push")
    commit_parser.add_argument("-m", "--message", help="Commit message")
    commit_parser.add_argument("branch", nargs="?", default="", help="Branch to push to (optional)")
    commit_parser.set_defaults(func=commit, _type="static")

    # Repo command
    repo_parser = subparsers.add_parser("repo", help="Create new repo and push")
    repo_parser.add_argument("url", help="Remote origin URL")
    repo_parser.set_defaults(func=repo, _type="static")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create new shortcut")
    create_parser.add_argument("name", help="Shortcut name")
    create_parser.add_argument("variables", help="Variables as 'var1,var2'")
    create_parser.add_argument("commands", nargs="+", help="Commands to run")
    create_parser.set_defaults(func=create, _type="static")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete shortcut")
    delete_parser.add_argument("name", help="Shortcut name to delete")
    delete_parser.set_defaults(func=delete, _type="static")

    # List command
    list_parser = subparsers.add_parser("list", help="List all shortcuts")
    list_parser.set_defaults(func=list_shortcuts, _type="static")

    # Dynamic shortcuts
    for shortcut in data.get("shortcuts", []):
        sc_parser = subparsers.add_parser(shortcut["name"], help=f"Shortcut: {shortcut['name']}")
        for var in shortcut.get("args", []):
            sc_parser.add_argument(var)
        sc_parser.set_defaults(
            func=run_dynamic_shortcut, 
            func_name=shortcut["name"], 
            _type="dynamic", 
            _data=data
        )

    return parser

def main():
    """Main function"""
    parser = build_parser_with_dynamic_subcommands()
    args = parser.parse_args()

    if hasattr(args, "func"):
        try:
            if getattr(args, "_type", "") == "dynamic":
                args.func(args, args._data)
            else:
                args.func(args)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()