# SDhunter – The Subdomain Enumeration Tool 
SDhunter is a lightweight and practical **subdomain enumeration tool** written in Python, designed for **penetration testers and offensive security professionals**.  
It focuses on **DNS-based discovery**, optional **HTTP probing**, and **virtual host enumeration**, without unnecessary complexity or heavy dependencies.

SDhunter is built to be fast, readable, and easily extendable—ideal for reconnaissance during penetration tests and bug bounty assessments.

---

## Features

- DNS-based subdomain enumeration using wordlists  
- Optional HTTP probing to identify live web services  
- Virtual host (vhost) discovery using custom `Host` headers    
- Output saved to a separate file  
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

## Installation & Usage Guide

### Requirements

- Python 3.7+
- `requests` library

Install the dependency:

```bash
pip install requests
```

### Clone the repository:

```bash
git clone https://github.com/Sh34iF-exe/sdhunter-Subdomain-finder.git
cd sdhunter
```
### Basic Subdomain Enumeration
```bash
python sdhunter.py -d example.com -w wordlist.txt
```
OR
```bash
python3 sdhunter.py -d example.com -w wordlist.txt
```
This performs DNS resolution for each subdomain generated from the wordlist.

## Available Command-Line Options

| Option | Description |
|--------|------------|
| `-d, --domain` | Target domain (e.g. example.com) |
| `-w, --wordlist` | Wordlist file for subdomain enumeration |
| `-o, --output` | Save results to an output file |
| `--http` | Enable HTTP probing for discovered subdomains |
| `--vhost` | Base URL for virtual host testing |

For a complete and authoritative list of options, run:
```bash
python3 sdhunter.py --help
```

## Disclaimer

SDhunter is intended for authorized security testing only.
The author is not responsible for misuse or damage caused by this tool.
Always ensure you have explicit permission before testing any target systems or domains.

### Author
Sh34iF.exe

### License
MIT License

## Contribution

Contributions are welcome and appreciated.

To contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with a clear message
4. Submit a pull request describing your changes

Please keep contributions focused, minimal, and aligned with SDhunter’s lightweight design philosophy.
