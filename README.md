# SDhunter – Subdomain Enumeration Tool for Pentesters

SDhunter is a lightweight and practical **subdomain enumeration tool** written in Python, designed for **penetration testers and offensive security professionals**.  
It focuses on **DNS-based discovery**, optional **HTTP probing**, and **virtual host enumeration**, without unnecessary complexity or heavy dependencies.

SDhunter is built to be fast, readable, and easily extendable—ideal for reconnaissance during penetration tests and bug bounty assessments.

---

## Features

- DNS-based subdomain enumeration using wordlists  
- Optional HTTP probing to identify live web services  
- Virtual host (vhost) discovery using custom `Host` headers  
- Clean Linux-style ASCII banner  
- Output saved to a separate file  
- Single-file implementation (easy to audit and modify)  
- Minimal dependencies  

---

## Why SDhunter?

Many subdomain tools are either:
- Overly complex
- Heavy on dependencies
- Focused on passive sources only

SDhunter takes a **hands-on, active reconnaissance approach**:
- It resolves subdomains using DNS (not just HTTP)
- It allows direct virtual host testing
- It fits naturally into real-world pentesting workflows

---

## Installation

### Requirements

- Python 3.7+
- `requests` library

Install the dependency:

```bash
pip install requests

