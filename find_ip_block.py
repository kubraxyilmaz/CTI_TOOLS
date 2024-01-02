import requests
import ipaddress

def get_ip_blocks(api_key, org_name):
    api_url = "https://ip-netblocks.whoisxmlapi.com/api/v2"
    params = {"apiKey": api_key, "org[]": org_name}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        ip_blocks_all = [item["inetnum"] for item in data["result"]["inetnums"]]
        return ip_blocks_all
    else:
        print(f"API request failed. Status code: {response.status_code}")
        return None

def ip_range_to_cidr(start_ip, end_ip):
    try:
        start_ip_obj = ipaddress.ip_address(start_ip)
        end_ip_obj = ipaddress.ip_address(end_ip)

        cidr_notation = ipaddress.summarize_address_range(start_ip_obj, end_ip_obj)

        return cidr_notation

    except ipaddress.AddressValueError:
        print(f"Invalid IP address: {start_ip} or {end_ip}")
        return None

# API key ve organizasyon adını buraya ekleyin
api_key = "YOUR API_KEY"
org_name = input("netname nedir? : ")

# IP bloklarını al
ip_blocks = get_ip_blocks(api_key, org_name)

# Sonuçları göster
if ip_blocks:
    print("CIDR Notasyonu:")
    for ip_range in ip_blocks:
        start_ip, end_ip = ip_range.split(" - ")
        cidr_notation = ip_range_to_cidr(start_ip, end_ip)
        if cidr_notation:
            for cidr in cidr_notation:
                print(cidr)
