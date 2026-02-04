import argparse
import socket
import requests
from datetime import datetime


# -------------------------
# Banner
# -------------------------
def banner():
    print(r"""
          
  /$$$$$$  /$$$$$$$  /$$                             /$$                        
 /$$__  $$| $$__  $$| $$                            | $$                        
| $$  \__/| $$  \ $$| $$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
|  $$$$$$ | $$  | $$| $$__  $$| $$  | $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$
 \____  $$| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$  | $$    | $$$$$$$$| $$  \__/
 /$$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$      
|  $$$$$$/| $$$$$$$/| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$$| $$      
 \______/ |_______/ |__/  |__/ \______/ |__/  |__/   \___/   \_______/|__/      
                                                                                
                                                                                                                                                               
                                                    Subdomain Enumerator
                                                        - by Sh34iF.exe
""")

# -------------------------
# Output Writer
# -------------------------
def write_output(filename, content):
    if filename:
        with open(filename, "a") as f:
            f.write(content + "\n")


# -------------------------
# DNS Subdomain Enumeration
# -------------------------
def dns_enum(domain, wordlist, output_file):
    found = []

    print("[+] Starting DNS enumeration...\n")
    write_output(output_file, "[DNS Results]")
    write_output(output_file, "-" * 30)

    for word in wordlist:
        subdomain = f"{word}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            result = f"{subdomain} -> {ip}"
            print(f"[DNS] Found: {result}")
            write_output(output_file, result)
            found.append(subdomain)
        except socket.gaierror:
            continue

    return found


# -------------------------
# HTTP Probing (Optional)
# -------------------------
def http_probe(subdomains, output_file):
    print("\n[+] HTTP probing...\n")
    write_output(output_file, "\n[HTTP Probe Results]")
    write_output(output_file, "-" * 30)

    for sub in subdomains:
        url = f"http://{sub}"
        try:
            r = requests.get(url, timeout=5, allow_redirects=True)
            result = f"{url} -> {r.status_code}"
            print(f"[HTTP] {result}")
            write_output(output_file, result)
        except requests.exceptions.RequestException:
            continue


# -------------------------
# Virtual Host Discovery
# -------------------------
def vhost_enum(base_url, wordlist, output_file):
    print("\n[+] Virtual host discovery...\n")
    write_output(output_file, "\n[Virtual Host Findings]")
    write_output(output_file, "-" * 30)

    for word in wordlist:
        headers = {
            "Host": word
        }

        try:
            r = requests.get(base_url, headers=headers, timeout=5)
            if r.status_code != 404 and len(r.text) > 0:
                result = f"Possible virtual host: {word}"
                print(f"[VHOST] {result}")
                write_output(output_file, result)
        except requests.exceptions.RequestException:
            continue


# -------------------------
# Main
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="Simple Subdomain Enumerator for Pentesters")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    parser.add_argument("-o", "--output", help="Output file to save results")
    parser.add_argument("--http", action="store_true", help="Enable HTTP probing")
    parser.add_argument("--vhost", help="Base URL for virtual host testing (e.g. http://example.com)")

    args = parser.parse_args()

    banner()

    print(f"[+] Target domain : {args.domain}")
    print(f"[+] Wordlist      : {args.wordlist}")
    if args.output:
        print(f"[+] Output file   : {args.output}")

    if args.output:
        with open(args.output, "w") as f:
            f.write("Subdomain Enumerator Results\n")
            f.write("=" * 35 + "\n")
            f.write(f"Target Domain : {args.domain}\n")
            f.write(f"Scan Time     : {datetime.now()}\n\n")

    with open(args.wordlist, "r") as f:
        words = [line.strip() for line in f if line.strip()]

    found_subdomains = dns_enum(args.domain, words, args.output)

    if args.http:
        http_probe(found_subdomains, args.output)

    if args.vhost:
        vhost_enum(args.vhost, words, args.output)

    print("\n[+] Enumeration completed.")


if __name__ == "__main__":
    main()