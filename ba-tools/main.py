import tkinter as tk
from pathlib import Path 

# that is the ba-tools folder
ROOT_PATH = Path(__file__).parent 

if __name__ == '__main__': 
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    tk.mainloop()