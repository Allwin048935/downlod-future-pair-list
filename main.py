from binance.client import Client

api_key = "Hqod6Y5MDAkMmAJbRKOqUUDsYb9HG5aAkE3BMPZxHrm8JdZTgfIJr2RKSkRiOlDM"
api_secret = "wVI5YTy9Y3dhiU1KoOSc0ysMVsAvaklSHDm40ZqkaHzKGgjlq9zlmi5CSF3n2wGw"

client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()

futures_trading_pairs = [s['symbol'] for s in exchange_info['symbols'] if s['symbol'].endswith('USDT')]

for trading_pair in futures_trading_pairs:
    print(trading_pair)
