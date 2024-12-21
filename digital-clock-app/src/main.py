import tkinter as tk
from gui.clock import Clock

def main():
    root = tk.Tk()
    root.title("Kell")
    fixed_width = 300  # Set your desired fixed width
    root.minsize(width=fixed_width, height=65)
    root.maxsize(width=fixed_width, height=65)
    clock = Clock(root)
    root.mainloop()

if __name__ == "__main__":
    main()