import tkinter as tk
import time
from tkinter import font

class Clock:
    def __init__(self, master):
        self.master = master
        self.font = font.Font(family="ds-digital", size=48)
        self.label = tk.Label(master, font=self.font, bg="#0d0d0d", fg="#00ffcc", width=10)  # Fixed width for time display
        self.label.pack(anchor='center')
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.master.after(1000, self.update_clock)