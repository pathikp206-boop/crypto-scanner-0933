import requests
from config import BYBIT_URL


def get_symbols():
    url = f"{BYBIT_URL}/v5/market/instruments-info"

    params = {
        "category": "linear"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    print("STATUS:", response.status_code)
    print("URL:", response.url)
    print("HEADERS:", response.headers)
    print("BODY:")
    print(response.text)

    raise Exception("Stop here")