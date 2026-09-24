#!/usr/bin/env python3
"""
Installs a git hook that appends insertion/deletion stats to GitDoc's autosave
commit messages. Run once with: python3 .setup/setup-hooks.py
"""
import os
import shutil
import stat
import subprocess
import sys

HOOK_NAME = "prepare-commit-msg"
HOOK_SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), HOOK_NAME)
TEMPLATE_DIR = os.path.join(os.path.expanduser("~"), ".git-templates")


def install_into(hooks_dir):
    os.makedirs(hooks_dir, exist_ok=True)
    dest = os.path.join(hooks_dir, HOOK_NAME)
    shutil.copyfile(HOOK_SOURCE, dest)
    current_mode = os.stat(dest).st_mode
    os.chmod(dest, current_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    return dest


def main():
    if not os.path.isfile(HOOK_SOURCE):
        print(f"Couldn't find {HOOK_SOURCE} — run this script from inside cs50-workspace.")
        sys.exit(1)

    # Register a git template dir so every future `git clone`/`git init` gets the hook too.
    template_hooks = os.path.join(TEMPLATE_DIR, "hooks")
    install_into(template_hooks)
    subprocess.run(["git", "config", "--global", "init.templateDir", TEMPLATE_DIR], check=True)
    print(f"Registered template hooks dir: {template_hooks}")

    # Apply it to the current repo immediately, since it was already cloned before this ran.
    result = subprocess.run(["git", "rev-parse", "--git-dir"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Not inside a git repo — future clones will still get the hook.")
        return

    dest = install_into(os.path.join(result.stdout.strip(), "hooks"))
    print(f"Installed hook into this repo: {dest}")


if __name__ == "__main__":
    main()
