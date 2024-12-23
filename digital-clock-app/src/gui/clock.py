import tkinter as tk
import time
from tkinter import font

class Clock:
    """
    A class to represent a digital clock with time and date display.
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
        
        self.label_time = tk.Label(master, font=self.font_time, bg="#0d0d0d", fg="#00ffcc")
        self.label_time.pack(expand=True, fill='both')
        
        self.label_date = tk.Label(master, font=self.font_date, bg="#0d0d0d", fg="#00ffcc")
        self.label_date.pack(expand=True, fill='both')
        
        self.update_clock()
        self.master.bind('<Configure>', self.resize_font)

    def update_clock(self):
        """
        Update the time and date displayed on the clock.
        """
        current_time = time.strftime("%H:%M:%S")
        day = int(time.strftime("%d"))
        suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        current_date = time.strftime(f"%d{suffix} of %B, %Y")
        
        self.label_time.config(text=current_time)
        self.label_date.config(text=current_date)
        
        self.master.after(1000, self.update_clock)

    def resize_font(self, event):
        """
        Resize the font of the time and date labels based on the window size.

        Parameters:
        event (tk.Event): The event object containing information about the resize event.
        """
        new_size_time = max(min(event.width // 26, event.height // 4), 26)  # Ensure a minimum font size of 26
        new_size_date = max(min(event.width // 40, event.height // 10), 20)  # Ensure a minimum font size of 10
        
        self.font_time.configure(size=new_size_time)
        self.font_date.configure(size=new_size_date)