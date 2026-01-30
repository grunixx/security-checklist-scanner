from pathlib import Path

def run(project_path: Path):
    env_file = project_path / ".env"
    if env_file.exists():
        return ("warning", ".env file detected")
    return ("ok", "No .env file found")