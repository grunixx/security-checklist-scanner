import json
import sys
from pathlib import Path

from scanner.checks import secrets_check, gitignore_check

SEVERITY_ORDER = {
    "low": 1,
    "medium": 2,
    "high": 3
}

def calculate_global_severity(results):
    if any(r["severity"] == "high" for r in results):
        return "high"
    if any(r["severity"] == "medium" for r in results):
        return "medium"
    return "low"

def main():
    args = sys.argv[1:]

    output_json = "--json" in args
    output_pretty = "--pretty" in args or not output_json

    fail_on = None
    if "--fail-on" in args:
        idx = args.index("--fail-on")
        try:
            fail_on = args[idx + 1]
        except IndexError:
            print("Error: --fail-on requires a severity level (low|medium|high)")
            sys.exit(2)

    project_path = Path.cwd()
    for arg in args:
        if not arg.startswith("--"):
            project_path = Path(arg)

    results = []

    # Secrets check
    secrets_result = secrets_check.run(project_path)
    results.append({
        "check": "secrets_check",
        **secrets_result
    })

    # Gitignore check
    gitignore_result = gitignore_check.run(project_path)
    results.append({
        "check": "gitignore_check",
        **gitignore_result
    })

    global_severity = calculate_global_severity(results)

    output = {
        "project": str(project_path),
        "global_severity": global_severity,
        "results": results
    }

    if output_json:
        print(json.dumps(output, indent=2))
    else:
        print(f"\n🔍 Security Scan — Target: {project_path}")
        print(f"🚨 Global severity: {global_severity.upper()}\n")

        for r in results:
            print(f"• {r['check']}")
            print(f"  status: {r['status']}")
            print(f"  severity: {r['severity']}")
            print(f"  message: {r['message']}")

            if r.get("files"):
                for f in r["files"]:
                    print(f"    - {f['file']} ({f['severity']})")
            print()

    if fail_on:
        if SEVERITY_ORDER[global_severity] >= SEVERITY_ORDER[fail_on]:
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
