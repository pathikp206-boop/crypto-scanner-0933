from concurrent.futures import ThreadPoolExecutor, as_completed
from okx_api import get_symbols, get_klines
from indicators import add_indicators
import time


def scan_symbol(symbol):
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

            return {
                "symbol": symbol,
                "price": latest["close"],
                "rsi": round(latest["RSI"], 2),
                "atr": round(latest["ATR"], 2)
            }

    except Exception as e:
        print(f"{symbol}: {e}")

    return None


def run():

    symbols = get_symbols()

    print(f"\nScanning {len(symbols)} symbols...\n")

    start = time.time()

    candidates = []

    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = {
            executor.submit(scan_symbol, symbol): symbol
            for symbol in symbols
        }

        completed = 0

        for future in as_completed(futures):

            completed += 1

            if completed % 20 == 0:
                print(f"Progress: {completed}/{len(symbols)}")

            result = future.result()

            if result:
                candidates.append(result)

    end = time.time()

    candidates.sort(
        key=lambda x: x["rsi"],
        reverse=True
    )

    print("\n==============================")
    print("SCAN COMPLETE")
    print("==============================")

    print(f"Coins scanned : {len(symbols)}")
    print(f"Candidates    : {len(candidates)}")
    print(f"Time          : {end-start:.2f} sec")

    print("\nTop 20\n")

    for coin in candidates[:20]:

        print(
            f"{coin['symbol']} | "
            f"Price {coin['price']:.4f} | "
            f"RSI {coin['rsi']} | "
            f"ATR {coin['atr']}"
        )