import sys
import requests

def discover_subdomains(target_domain):
    subdomains = set()

    try:
        url = f"https://crt.sh/?q=%25.{target_domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()

        for entry in data:
            subdomain = entry.get("name_value")
            if subdomain:
                subdomain = subdomain.strip()
                if subdomain.startswith("*."):
                    subdomain = subdomain[2:]
                subdomains.add(subdomain)

    except Exception as e:
        print(f"Error discovering subdomains: {e}")

    return subdomains

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <target_domain>")
        sys.exit(1)

    target_domain = sys.argv[1]
    subdomains = discover_subdomains(target_domain)

    with open("crtsh_result.txt", 'w') as result_file:
        for subdomain in subdomains:
            result_file.write(subdomain + '\n')

    print(f"Results written to crtsh_result.txt")
