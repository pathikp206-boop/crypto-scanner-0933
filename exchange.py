import requests
from config import BYBIT_URL


def get_symbols():
    url = f"{BYBIT_URL}/v5/market/instruments-info"

    params = {
        "category": "linear"
    }

    response = requests.get(url, params=params, timeout=30)

    print(response.status_code)

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