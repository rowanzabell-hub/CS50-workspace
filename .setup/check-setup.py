#!/usr/bin/env python3
"""Checks that your CS50 workspace is set up correctly. Run with: python3 check-setup.py"""
import re
import shutil
import subprocess
import sys

REQUIRED_EXTENSIONS = {
    "vsls-contrib.gitdoc": "GitDoc (autosave)",
    "ms-python.python": "Python",
    "ms-python.autopep8": "autopep8",
    "ms-python.debugpy": "Python Debugger",
}

TEMPLATE_REPO = "mrsharp-milken/cs50-workspace"

GITDOC_COMMIT_RE = re.compile(
    r"^[A-Za-z]{3}, [A-Za-z]{3} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M"
)

passed, failed, warned = [], [], []


def ok(label, detail=""):
    passed.append(label)
    print(f"  [OK]   {label}" + (f" — {detail}" if detail else ""))


def fail(label, detail=""):
    failed.append(label)
    print(f"  [FAIL] {label}" + (f" — {detail}" if detail else ""))


def warn(label, detail=""):
    warned.append(label)
    print(f"  [WARN] {label}" + (f" — {detail}" if detail else ""))


def run(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except FileNotFoundError:
        return None, "", ""
    except subprocess.TimeoutExpired:
        return -1, "", "timed out"


def check_python():
    print("\nPython")
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.version_info[:2] >= (3, 13):
        ok("python3 version", version)
    else:
        warn("python3 version", f"{version} — the guide installs 3.13, tkinter may not work on older versions")

    try:
        import tkinter
        root = tkinter.Tk()
        root.withdraw()
        root.destroy()
        ok("tkinter", "graphics library working")
    except Exception as e:
        fail("tkinter", f"{e} — try reinstalling Python with the manual installer from python.org")


def check_git_gh():
    print("\nGit & GitHub CLI")
    if shutil.which("git"):
        ok("git installed")
    else:
        fail("git installed", "run: brew install git")
        return None

    if not shutil.which("gh"):
        fail("gh (GitHub CLI) installed", "run: brew install gh")
        return None
    ok("gh installed")

    code, _, _ = run(["gh", "auth", "status"])
    if code == 0:
        ok("gh authenticated")
    else:
        fail("gh authenticated", "run: gh auth login")
        return None

    code, login, _ = run(["gh", "api", "user", "--jq", ".login"])
    if code != 0 or not login:
        warn("could not look up GitHub username", "skipping git config checks")
        return None

    _, name, _ = run(["git", "config", "--global", "user.name"])
    if name == login:
        ok("git config user.name", name)
    else:
        fail("git config user.name", f"expected '{login}', found '{name or '(not set)'}'")

    _, email, _ = run(["git", "config", "--global", "user.email"])
    if email and email.endswith("@users.noreply.github.com") and login in email:
        ok("git config user.email", email)
    else:
        fail("git config user.email", f"found '{email or '(not set)'}' — see the Autosaving section of the README")

    return login


def check_repo(login):
    print("\nThis repository")
    code, _, _ = run(["git", "rev-parse", "--is-inside-work-tree"])
    if code != 0:
        warn("not inside a git repo", "run this from inside your cs50-workspace folder")
        return

    code, url, _ = run(["git", "remote", "get-url", "origin"])
    if code != 0 or not url:
        fail("git remote 'origin' configured", "see the Autosaving section of the README")
    elif TEMPLATE_REPO in url:
        fail("git remote 'origin'", "points at the template repo — did you clone your own copy instead of the original?")
    else:
        ok("git remote 'origin'", url)

    code, log, _ = run(["git", "log", "-5", "--pretty=%s"])
    if code != 0 or not log:
        fail("recent commits", "no commits found yet")
    else:
        messages = log.splitlines()
        if any(GITDOC_COMMIT_RE.match(m) or m.strip() == "first commit" for m in messages):
            ok("recent commits", "GitDoc autosave detected")
        else:
            warn("GitDoc autosave commits not detected yet", "edit a file and wait ~20 seconds, then re-run this script")


STUDENT_PROFILES = ["mrsharp-student", "cs50 student"]


def check_extensions():
    print("\nVSCodium extensions")
    codium = shutil.which("codium")
    if not codium:
        warn(
            "could not check installed extensions",
            "open VSCodium, Cmd+Shift+P, run 'Shell Command: Install codium command in PATH', then re-run this script",
        )
        return

    code, output, _ = run([codium, "--list-extensions"])
    if code != 0:
        warn("could not list extensions", output or "unknown error")
        return

    installed = set(output.splitlines())

    # Extensions imported via a .code-profile land in an isolated profile, not
    # the Default one, and are only active in the GUI once that workspace is
    # opened — so also check the profile(s) students may have imported.
    for profile in STUDENT_PROFILES:
        code, output, _ = run([codium, "--list-extensions", "--profile", profile])
        if code == 0:
            installed |= set(output.splitlines())

    for ext_id, label in REQUIRED_EXTENSIONS.items():
        if ext_id in installed:
            ok(label)
        else:
            fail(label, f"extension '{ext_id}' not found — re-import the profile from the README")


def main():
    print("Checking your CS50 workspace setup...")
    check_python()
    login = check_git_gh()
    check_repo(login)
    check_extensions()

    print(f"\n{len(passed)} passed, {len(warned)} warnings, {len(failed)} failed")
    if failed:
        print("\nFix the [FAIL] items above, then run this script again.")
        sys.exit(1)
    elif warned:
        print("\nLooks mostly good — take a look at the [WARN] items above.")
    else:
        print("\nEverything looks good!")


if __name__ == "__main__":
    main()
