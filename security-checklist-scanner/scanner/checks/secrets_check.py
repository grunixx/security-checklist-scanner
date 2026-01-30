from pathlib import Path
import re

IGNORED_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build"
}

SECRET_PATTERNS = [
    (
        re.compile(r"api[_-]?key\s*=\s*['\"].+['\"]", re.IGNORECASE),
        "medium"
    ),
    (
        re.compile(r"secret\s*=\s*['\"].+['\"]", re.IGNORECASE),
        "high"
    ),
    (
        re.compile(r"token\s*=\s*['\"].+['\"]", re.IGNORECASE),
        "high"
    ),
    (
        re.compile(r"password\s*=\s*['\"].+['\"]", re.IGNORECASE),
        "high"
    ),
]

ALLOWED_SUFFIXES = {".py", ".js", ".ts", ".env"}

def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)

def run(project_path: Path):
    """
    Scans source files for possible hardcoded secrets using regex patterns.
    Ignores common build and dependency directories.
    """
    findings = []

    for path in project_path.rglob("*"):
        if is_ignored(path):
            continue

        if not path.is_file() or path.suffix not in ALLOWED_SUFFIXES:
            continue

        try:
            content = path.read_text(errors="ignore")
        except Exception:
            continue

        for pattern, severity in SECRET_PATTERNS:
            if pattern.search(content):
                findings.append({
                    "file": str(path),
                    "severity": severity
                })
                break

    if findings:
        highest_severity = "low"

        if any(f["severity"] == "high" for f in findings):
            highest_severity = "high"
        elif any(f["severity"] == "medium" for f in findings):
            highest_severity = "medium"

        return {
            "status": "warning",
            "severity": highest_severity,
            "message": "Possible hardcoded secrets found",
            "files": findings
        }

    return {
        "status": "ok",
        "severity": "low",
        "message": "No hardcoded secrets detected",
        "files": []
    }
