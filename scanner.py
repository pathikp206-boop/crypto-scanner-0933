from okx_api import get_symbols, get_klines
from indicators import add_indicators


def run():

    symbols = get_symbols()

    print(f"Scanning {len(symbols)} symbols...\n")

    candidates = []

    for symbol in symbols:

        try:

            df = get_klines(symbol)

            df = add_indicators(df)

            latest = df.iloc[-2]

            if (
                latest["close"] > latest["EMA20"]
                and latest["EMA20"] > latest["EMA50"]
                and latest["EMA50"] > latest["EMA200"]
                and latest["RSI"] > 55
            ):

                candidates.append(
                    {
                        "symbol": symbol,
                        "price": latest["close"],
                        "rsi": round(latest["RSI"], 1),
                        "atr": round(latest["ATR"], 2)
                    }
                )

        except Exception as e:

            print(symbol, e)

    print("\nCandidates Found:", len(candidates))

    for coin in candidates:

        print(coin)