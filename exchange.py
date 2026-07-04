import requests
from config import BYBIT_URL


def get_symbols():
    url = f"{BYBIT_URL}/v5/market/instruments-info"

    params = {
        "category": "linear"
    }

    response = requests.get(
    url,
    params=params,
    timeout=30,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status:", response.status_code)
print("Headers:", response.headers)
print("Body:")
print(response.text)

if response.status_code != 200:
    raise Exception("HTTP Error")

data = response.json()

    if data["retCode"] != 0:
        raise Exception(data)

    symbols = []

    for s in data["result"]["list"]:

        if (
            s["status"] == "Trading"
            and s["quoteCoin"] == "USDT"
        ):
            symbols.append(s["symbol"])

    return sorted(symbols)