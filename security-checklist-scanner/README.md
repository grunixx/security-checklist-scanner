# 🔍 Security Checklist Scanner

A lightweight CLI tool that performs basic security checks on a project directory, helping developers quickly identify common security risks during early development stages.

This project is intentionally simple, readable, and extensible — designed both as a practical tool and as a learning-focused showcase for security-oriented tooling.

---

## 🚨 The Problem

Many security issues appear very early in software projects:

- Secrets accidentally committed to the repository  
- Missing or incomplete `.gitignore` files  
- Sensitive files tracked by version control  

Most existing security tools are powerful but heavy, complex, or difficult to customize.  
This project focuses on **early, low-friction security awareness**, especially for small projects, students, and prototypes.

---

## ✅ The Solution

**Security Checklist Scanner** scans a target directory and runs a set of modular security checks, producing a clear and readable CLI report with:

- Individual check results  
- Per-check severity levels  
- A calculated global severity  

The tool is designed to be:

- Easy to understand  
- Easy to extend  
- Safe to run locally  

---

## 🧠 How It Works

1. The user runs the CLI pointing to a project directory  
2. Each security check scans the project independently  
3. Results are normalized into a common format  
4. A global severity level is calculated  
5. Results are printed in a human-friendly CLI output (or JSON)

