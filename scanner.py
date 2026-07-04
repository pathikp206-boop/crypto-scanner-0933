from okx_api import get_symbols, get_klines
from indicators import add_indicators


def run():

    symbols = get_symbols()

    total = len(symbols)

    print("=" * 50)
    print(f"Scanning {total} symbols...")
    print("=" * 50)

    candidates = []

    for i, symbol in enumerate(symbols, start=1):

        print(f"[{i:03}/{total}] {symbol}")

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
                        "price": round(latest["close"], 4),
                        "rsi": round(latest["RSI"], 2),
                        "atr": round(latest["ATR"], 2)
                    }
                )

        except Exception as e:

            print(f"❌ {symbol}: {e}")

    print("\n" + "=" * 50)
    print("SCAN COMPLETE")
    print("=" * 50)

    print(f"Coins Scanned : {total}")
    print(f"Candidates    : {len(candidates)}")

    if candidates:

        print("\nTop Candidates\n")

        for coin in candidates:

            print(
                f"{coin['symbol']} | "
                f"Price: {coin['price']} | "
                f"RSI: {coin['rsi']} | "
                f"ATR: {coin['atr']}"
            )