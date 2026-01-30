# 🔍 Security Checklist Scanner

A lightweight CLI tool that performs basic security checks on a project directory, helping developers quickly identify common security risks during early development stages.

This project is intentionally simple, readable, and extensible, designed both as a practical tool and as a learning showcase for security-oriented tooling.

---

## 🚨 Problem

Many security issues appear very early in projects:

* Secrets accidentally committed to the repository
* Missing or incomplete `.gitignore` files
* Sensitive files tracked by version control

Most existing security tools are powerful but heavy, complex, or difficult to customize. This project focuses on **early, low-friction security awareness**, especially for small projects, students, and prototypes.

---

## ✅ Solution

**Security Checklist Scanner** scans a target directory and runs a set of modular security checks, producing a clear CLI report with:

* Individual check results
* Per-check severity
* A calculated global severity

The tool is designed to be:

* Easy to understand
* Easy to extend
* Safe to run locally

---

## 🧠 How It Works

1. The user runs the CLI pointing to a project directory
2. Each security check scans the project independently
3. Results are normalized into a common format
4. A global severity is calculated
5. Results are printed in a human-friendly CLI output (or JSON)

```
scanner/
├── main.py
├── runner.py
├── checks/
│   ├── secrets_check.py
│   └── gitignore_check.py
```

Each check exposes a `run(project_path: Path)` function and returns a structured result.

---

## 🔎 Implemented Checks

### 🔐 Secrets Check (`secrets_check`)

Scans source files for **possible hardcoded secrets**, such as:

* API keys
* Tokens
* Passwords

Features:

* Regex-based detection
* Severity classification (low / medium / high)
* Ignores common directories (`.git`, `node_modules`, `venv`, etc.)

Example output:

```
• secrets_check
  status: ok
  severity: low
  message: No hardcoded secrets detected
```

---

### 📁 Gitignore Check (`gitignore_check`)

Validates whether the project `.gitignore` includes common sensitive patterns, such as:

* `.env`
* `*.pem`
* `*.key`

If missing, the check raises a warning with medium severity.

Example output:

```
• gitignore_check
  status: warning
  severity: medium
  message: .gitignore missing sensitive entries: .env, *.env, *.pem
```

---

## ▶️ How to Run

From inside the `scanner` directory:

```bash
python main.py ..
```

### JSON output

```bash
python main.py .. --json
```

### Exit codes

* `0` → no high severity issues
* `1` → high severity issues detected

---

## 🧭 Roadmap

Planned improvements:

* Dependency vulnerability check
* File permission analysis
* Configurable severity thresholds
* Custom rule definitions
* CI/CD integration example

---

## 🎯 Goals

This project is both:

* A **practical security utility**
* A **portfolio-quality demonstration** of clean Python architecture, CLI design, and security thinking

---

## 📄 License

MIT License
