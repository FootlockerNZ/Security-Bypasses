# Ticketmaster OPTIONS Method Bypass PoC

## 🔍 Overview

This project demonstrates a security bypass on Ticketmaster New Zealand's website. While standard `GET` requests are subject to bot protection and often return obfuscated or blocked responses, an `OPTIONS` request—typically used in CORS preflight checks—unexpectedly returns the full raw HTML content of the homepage. This suggests a misconfiguration or gap in bot mitigation and caching layers.

## 🚧 Purpose

This proof of concept (PoC) showcases technical insight into HTTP method handling and highlights how non-standard request methods can unintentionally bypass bot detection systems and content delivery rules. It is intended for educational and ethical research purposes only.

## ⚙️ Technical Details

- **Target:** `https://www.ticketmaster.co.nz/`
- **Issue:** Standard `GET` requests are intercepted by a security or caching layer.
- **Bypass:** Sending an `OPTIONS` request returns plaintext HTML, bypassing the bot protections.
- **Potential Cause:** Method-based filtering, misconfigured CORS preflight handling, or improperly cached origin responses.

## 🧪 Demonstration Code

```python
import requests

def fetch_ticketmaster_html():
    url = 'https://www.ticketmaster.co.nz/'

    # Attempt standard GET request
    get_resp = requests.get(url)
    print(f"[GET] Status: {get_resp.status_code}")
    print("[GET] Response Snippet:", get_resp.text))

    # Attempt OPTIONS request
    options_resp = requests.options(url)
    print(f"[OPTIONS] Status: {options_resp.status_code}")
    print("[OPTIONS] Response Snippet:")
    print(options_resp.text[:500])  # Show only the first 500 chars

if __name__ == "__main__":
    fetch_ticketmaster_html()
```

## ✅ Observations

- `GET` requests may return a security challenge or empty content.
- `OPTIONS` requests return full HTML content with status 200.
- Indicates insufficient bot filtering on non-GET methods.

## 🔒 Disclaimer

This code is for **educational use only**. Do not use it for unauthorized scraping, bypassing terms of service, or malicious activity. Always act in accordance with responsible disclosure guidelines.
