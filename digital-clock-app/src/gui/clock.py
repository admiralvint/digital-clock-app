import tkinter as tk
import time
import requests
from tkinter import font

API_KEY = '92409287-8d8c-4161-888c-c29c73558aa4'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def get_crypto_data(symbol):
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
    price = data['data'][symbol]['quote']['USD']['price']
    change_24h = data['data'][symbol]['quote']['USD']['percent_change_24h']
    return price, change_24h

class Clock:
    """
    A class to represent a digital clock with time, date, and cryptocurrency prices.
    """

    def __init__(self, master):
        """
        Initialize the Clock class.

        Parameters:
        master (tk.Tk): The root window of the Tkinter application.
        """
        self.master = master
        self.font_time = font.Font(family="ds-digital", size=58)
        self.font_date = font.Font(family="ds-digital", size=20)
        self.font_crypto = font.Font(family="ds-digital", size=20)
        
        self.label_time = tk.Label(master, font=self.font_time, bg="#0d0d0d", fg="#00ffcc")
        self.label_time.pack(expand=True, fill='both')
        
        self.label_date = tk.Label(master, font=self.font_date, bg="#0d0d0d", fg="#00ffcc")
        self.label_date.pack(expand=True, fill='both')
        
        self.label_btc = tk.Label(master, font=self.font_crypto, bg="#0d0d0d", fg="#FFD700")
        self.label_btc.pack(expand=True, fill='both')
        
        self.label_eth = tk.Label(master, font=self.font_crypto, bg="#0d0d0d", fg="#FFD700")
        self.label_eth.pack(expand=True, fill='both')
        
        self.update_clock()
        self.master.bind('<Configure>', self.resize_font)

    def update_clock(self):
        """
        Update the time, date, and cryptocurrency prices displayed on the clock.
        """
        current_time = time.strftime("%H:%M:%S")
        day = int(time.strftime("%d"))
        suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        current_date = time.strftime(f"%d{suffix} of %B, %Y")
        
        btc_price, btc_change = get_crypto_data('BTC')
        eth_price, eth_change = get_crypto_data('ETH')
        
        self.label_time.config(text=current_time)
        self.label_date.config(text=current_date)
        self.label_btc.config(text=f"BTC: ${btc_price:.2f} ({btc_change:+.2f}%)")
        self.label_eth.config(text=f"ETH: ${eth_price:.2f} ({eth_change:+.2f}%)")
        
        self.master.after(60000, self.update_clock)  # Update every 60 seconds

    def resize_font(self, event):
        """
        Resize the font of the time, date, and cryptocurrency labels based on the window size.

        Parameters:
        event (tk.Event): The event object containing information about the resize event.
        """
        new_size_time = max(min(event.width // 26, event.height // 4), 26)  # Ensure a minimum font size of 26
        new_size_date = max(min(event.width // 40, event.height // 10), 20)  # Ensure a minimum font size of 10
        new_size_crypto = max(min(event.width // 40, event.height // 10), 16)  # Ensure a minimum font size of 10
        
        self.font_time.configure(size=new_size_time)
        self.font_date.configure(size=new_size_date)
        self.font_crypto.configure(size=new_size_crypto)