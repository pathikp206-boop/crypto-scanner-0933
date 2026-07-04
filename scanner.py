from telegram_bot import send_message
from binance_api import get_symbols


def run():

    symbols = get_symbols()

    message = f"""
📡 Binance Connected

Exchange : Binance Futures

USDT Pairs : {len(symbols)}

Status : ✅ Ready
"""

    send_message(message)

    print(message)