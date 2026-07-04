from okx_api import get_klines
from indicators import add_indicators

df = get_klines("BTC-USDT-SWAP")

df = add_indicators(df)

print(df.tail())