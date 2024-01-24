from binance.client import Client
import sys

api_key = "BVhb32XgQmX17IGs3vVH2Hw1fiH9W84pg8K5JtLuQnRKHPy7YlyPTG0qChkxTnrL"
api_secret = "xVM8dF8qIhTRtfaTShbHON7oJffooUbP2wp3oPqYUbFLJ1ZCHLN9dEmN9niAYzVF"

client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()

futures_trading_pairs = [s['symbol'] for s in exchange_info['symbols']]

# Redirect stdout to a file
with open('output.txt', 'w') as f:
    sys.stdout = f

    for trading_pair in futures_trading_pairs:
        print(trading_pair)

# Reset stdout to the default (console) after writing to the file
sys.stdout = sys.__stdout__
