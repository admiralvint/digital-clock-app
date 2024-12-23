import tkinter as tk
from gui.clock import Clock

def main():
    """
    Main function to initialize and run the digital clock application.
    """
    root = tk.Tk()
    root.title("Crypto'O'Clock")
    clock = Clock(root)
    root.mainloop()

if __name__ == "__main__":
    main()