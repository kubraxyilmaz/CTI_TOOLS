import requests
import sys

def read_api_key(api_key_label, file_path="api_keys.txt"):
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith(f"{api_key_label}="):
                    return line[len(api_key_label)+1:]
            print(f"{api_key_label} bulunamadı.")
            sys.exit(1)
    except FileNotFoundError:
        print(f"{file_path} dosyası bulunamadı.")
        sys.exit(1)

# Komut satırından hedef domain bilgisini al
if len(sys.argv) != 2:
    print("Kullanım: python subdomain.py <hedef_domain>")
    sys.exit(1)

target_domain = sys.argv[1]
securitytrails_api_key = read_api_key("SECURITYTRAILS_API_KEY")

url = f"https://api.securitytrails.com/v1/domain/{target_domain}/subdomains?children_only=false&include_inactive=true"

headers = {
    "accept": "application/json",
    "APIKEY": securitytrails_api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Subdomain'leri birleştirip ekrana yazdır
    subdomains = data.get("subdomains", [])
    for subdomain in subdomains:
        full_domain = f"{subdomain}.{target_domain}"
        print(full_domain)
else:
    print(f"Hata {response.status_code}: {response.text}")

# ...

if response.status_code == 200:
    data = response.json()

    # Subdomain'leri birleştirip ekrana yazdır
    subdomains = data.get("subdomains", [])

    # Sonuçları dosyaya yaz
    output_file_path = "securitytrailsresult.txt"
    with open(output_file_path, "w") as output_file:
        for subdomain in subdomains:
            full_domain = f"{subdomain}.{target_domain}"
            print(full_domain)
            output_file.write(full_domain + "\n")

else:
    print(f"Hata {response.status_code}: {response.text}")

