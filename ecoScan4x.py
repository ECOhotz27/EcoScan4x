import requests import sys import json import csv from datetime import datetime

Colors for output

RED = "\033[91m" GREEN = "\033[92m" YELLOW = "\033[93m" CYAN = "\033[96m" RESET = "\033[0m"

Security headers and associated risk

security_headers = { "Content-Security-Policy": "High", "X-Frame-Options": "Medium", "X-XSS-Protection": "Medium", "Strict-Transport-Security": "High" }

Print banner

def print_banner(): print(f"""{CYAN} ███████╗ ██████╗ ██████╗     ███████╗ █████╗ ███╗   ██╗ ██╔════╝██╔═══██╗██╔══██╗    ██╔════╝██╔══██╗████╗  ██║ ███████╗██║   ██║██████╔╝    █████╗  ███████║██╔██╗ ██║ ╚════██║██║   ██║██╔═══╝     ██╔══╝  ██╔══██║██║╚██╗██║ ███████║╚██████╔╝██║         ██║     ██║  ██║██║ ╚████║ ╚══════╝ ╚═════╝ ╚═╝         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝ ecoScan4x - Security Header Scanner by @eco4x {RESET}""")

Analyze one URL

def analyze_url(url): result = {"URL": url} try: r = requests.get(url, timeout=10) result["Status Code"] = r.status_code result["HTTPS"] = url.startswith("https") headers = r.headers

missing = []
    found = []

    print(f"\n{CYAN}[+] Scanning: {url}{RESET}")
    print(f"Status Code: {r.status_code}")
    print(f"Uses HTTPS: {'Yes' if result['HTTPS'] else 'No'}")

    for header, risk in security_headers.items():
        if header in headers:
            print(f"{GREEN}[+] {header}: {headers[header]} (OK){RESET}")
            found.append({header: headers[header]})
        else:
            print(f"{RED}[-] {header}: Missing ({risk} Risk){RESET}")
            missing.append({"header": header, "risk": risk})

    result["Found Headers"] = found
    result["Missing Headers"] = missing
    result["Risk Level"] = "High" if any(h["risk"] == "High" for h in missing) else "Medium" if missing else "Low"

except Exception as e:
    print(f"{RED}[!] Error scanning {url}: {e}{RESET}")
    result["error"] = str(e)

return result

Save results

def save_results(results): timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") with open(f"scan_{timestamp}.txt", "w") as f: for r in results: f.write(json.dumps(r, indent=2) + "\n")

with open(f"scan_{timestamp}.json", "w") as f:
    json.dump(results, f, indent=2)

with open(f"scan_{timestamp}.csv", "w", newline="") as csvfile:
    fieldnames = ["URL", "Status Code", "HTTPS", "Risk Level"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in results:
        writer.writerow({
            "URL": r["URL"],
            "Status Code": r.get("Status Code", "Error"),
            "HTTPS": r.get("HTTPS", False),
            "Risk Level": r.get("Risk Level", "Unknown")
        })

Main

def main(): print_banner()

if len(sys.argv) != 2:
    print(f"{YELLOW}Usage: python ecoScan4x.py [target_url | targets.txt]{RESET}")
    sys.exit(1)

arg = sys.argv[1]
urls = []

if arg.startswith("http"):
    urls = [arg]
else:
    try:
        with open(arg, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
    except:
        print(f"{RED}[!] Failed to open file: {arg}{RESET}")
        sys.exit(1)

results = []
for url in urls:
    results.append(analyze_url(url))

save_results(results)
print(f"{GREEN}\n[+] Scan complete. Results saved in TXT, JSON, and CSV.{RESET}")

if name == "main": main()

