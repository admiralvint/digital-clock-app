import tkinter as tk
import requests
import time

API_KEY = '92409287-8d8c-4161-888c-c29c73558aa4'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def get_crypto_price(symbol):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }
    response = requests.get(URL, headers=headers, params=parameters)
    data = response.json()
    return data['data'][symbol]['quote']['USD']['price']

class CryptoPriceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Crypto Price App")
        self.label_btc = tk.Label(master, font=("Helvetica", 24), fg="white", bg="black")
        self.label_btc.pack(pady=10)
        self.label_eth = tk.Label(master, font=("Helvetica", 24), fg="white", bg="black")
        self.label_eth.pack(pady=10)
        self.update_prices()

    def update_prices(self):
        btc_price = get_crypto_price('BTC')
        eth_price = get_crypto_price('ETH')
        self.label_btc.config(text=f"Bitcoin (BTC): ${btc_price:.2f}")
        self.label_eth.config(text=f"Ethereum (ETH): ${eth_price:.2f}")
        self.master.after(60000, self.update_prices)  # Update every 60 seconds

def main():
    root = tk.Tk()
    app = CryptoPriceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()