from scanner.checks.env_check import run as env_check
from scanner.checks.secrets_check import run as secrets_check
from scanner.checks.gitignore_check import run as gitignore_check


def run_all_checks(project_path):
    results = []

    results.append(env_check(project_path))
    results.append(gitignore_check(project_path))
    results.append(secrets_check(project_path))

    return results