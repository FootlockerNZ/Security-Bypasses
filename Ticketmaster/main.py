import requests

def fetch_ticketmaster_html():
    url = 'https://www.ticketmaster.co.nz/'

    # Standard GET request: likely intercepted by WAF or bot challenge
    get_resp = requests.get(url)
    print(f"[GET] Status: {get_resp.status_code}")
    print("[GET] Length:", len(get_resp.text))

    print()

    # OPTIONS request bypass: may return full HTML response
    options_resp = requests.options(url)
    print(f"[OPTIONS] Status: {options_resp.status_code}")
    print("[OPTIONS] Response Snippet:")
    print(options_resp.text[:500])  # Limit output for readability

if __name__ == "__main__":
    fetch_ticketmaster_html()
