import requests
from config import OKX_URL


def get_symbols():

    url = f"{OKX_URL}/api/v5/public/instruments"

    params = {
        "instType": "SWAP"
    }

    response = requests.get(url, params=params, timeout=30)

    print("Status:", response.status_code)

    data = response.json()

    if data["code"] != "0":
        raise Exception(data)

    symbols = []

    for s in data["data"]:

        if (
            s["state"] == "live"
            and s["settleCcy"] == "USDT"
        ):
            symbols.append(s["instId"])

    return sorted(symbols)