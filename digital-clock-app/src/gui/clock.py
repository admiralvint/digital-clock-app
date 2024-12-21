import tkinter as tk
import time
from tkinter import font

class Clock:
    def __init__(self, master):
        self.master = master
        self.font = font.Font(family="ds-digital", size=58)
        self.label = tk.Label(master, font=self.font, bg="#0d0d0d", fg="#00ffcc")
        self.label.pack(expand=True, fill='both')
        self.update_clock()
        self.master.bind('<Configure>', self.resize_font)

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.master.after(1000, self.update_clock)

    def resize_font(self, event):
        new_size = max(min(event.width // 26, event.height // 2), 26)  # Ensure a minimum font size of 26
        self.font.configure(size=new_size)