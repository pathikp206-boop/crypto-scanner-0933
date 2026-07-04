import requests
import pandas as pd
from config import OKX_URL, LIMIT, TIMEFRAME


def get_symbols():
    url = f"{OKX_URL}/api/v5/public/instruments"

    params = {
        "instType": "SWAP"
    }

    response = requests.get(url, params=params, timeout=30)

    

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


def get_klines(symbol):
    url = f"{OKX_URL}/api/v5/market/candles"

    params = {
        "instId": symbol,
        "bar": TIMEFRAME,
        "limit": LIMIT
    }

    response = requests.get(url, params=params, timeout=30)

    data = response.json()

    if data["code"] != "0":
        raise Exception(data)

    df = pd.DataFrame(
        data["data"],
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "volCcy",
            "volCcyQuote",
            "confirm"
        ]
    )

    # Oldest candle first
    df = df.iloc[::-1].reset_index(drop=True)

    # Convert numeric columns
    numeric = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "volCcy",
        "volCcyQuote"
    ]

    df[numeric] = df[numeric].astype(float)

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(
        df["timestamp"].astype("int64"),
        unit="ms"
    )

    # Convert confirm flag
    df["confirm"] = df["confirm"].astype(int)

    return df