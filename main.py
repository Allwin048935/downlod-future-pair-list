from bybit.client import Client

api_key = "jcTIZOTsd1OsUOpgER"
api_secret = "IlBRdxegRqhkWFyHWs2K9omWXTuCDyLEx7a6"
client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()

futures_trading_pairs = [s['symbol'] for s in exchange_info['symbols'] if s['symbol'].endswith('USDT')]

for trading_pair in futures_trading_pairs:
    print(trading_pair)
