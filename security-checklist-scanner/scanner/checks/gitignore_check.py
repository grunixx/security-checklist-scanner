from pathlib import Path

SENSITIVE_PATTERNS = [
    ".env",
    "*.env",
    "*.pem",
    "*.key",
    "*.crt"
]

def run(project_path: Path):
    gitignore_path = project_path / ".gitignore"

    if not gitignore_path.exists():
        return {
            "status": "warning",
            "severity": "medium",
            "message": "No .gitignore file found",
            "files": []
        }

    try:
        content = gitignore_path.read_text()
    except Exception:
        return {
            "status": "warning",
            "severity": "medium",
            "message": "Unable to read .gitignore file",
            "files": []
        }

    missing = []

    for pattern in SENSITIVE_PATTERNS:
        if pattern not in content:
            missing.append(pattern)

    if missing:
        return {
            "status": "warning",
            "severity": "medium",
            "message": f".gitignore missing sensitive entries: {', '.join(missing)}",
            "files": [
                {"file": ".gitignore", "severity": "medium"}
            ]
        }

    return {
        "status": "ok",
        "severity": "low",
        "message": ".gitignore properly configured",
        "files": []
    }
