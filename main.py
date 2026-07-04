from okx_api import get_symbols

symbols = get_symbols()

print(len(symbols))

print(symbols[:20])