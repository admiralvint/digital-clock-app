import tkinter as tk
from gui.clock import Clock

def main():
    root = tk.Tk()
    root.title("Vindikell")
    clock = Clock(root)
    root.mainloop()

if __name__ == "__main__":
    main()