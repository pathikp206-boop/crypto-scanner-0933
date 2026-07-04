from okx_api import get_klines

df = get_klines("BTC-USDT-SWAP")

print(df.head())

print(df.tail())

print(df.dtypes)