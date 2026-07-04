import requests
from config import BINANCE_FUTURES


def get_symbols():

    url = f"{BINANCE_FUTURES}/fapi/v1/exchangeInfo"

    response = requests.get(url, timeout=30)

    print("Status:", response.status_code)
    print("Response:", response.text[:1000])

    data = response.json()

    if "symbols" not in data:
        raise Exception(f"Unexpected Binance response: {data}")

    symbols = []

    for s in data["symbols"]:
        if (
            s["contractType"] == "PERPETUAL"
            and s["quoteAsset"] == "USDT"
            and s["status"] == "TRADING"
        ):
            symbols.append(s["symbol"])

    return symbols