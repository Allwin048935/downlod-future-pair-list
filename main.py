import requests

def get_binance_futures_trading_pairs():
    base_url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        trading_pairs = [symbol['symbol'] for symbol in data['symbols'] if symbol['contractType'] == 'PERPETUAL']
        return trading_pairs
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def save_to_txt_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    trading_pairs = get_binance_futures_trading_pairs()

    if trading_pairs:
        save_to_txt_file(trading_pairs, "binance_futures_trading_pairs.txt")
