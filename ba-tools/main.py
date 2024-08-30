import tkinter as tk
from pathlib import Path 

# that is the ba-tools folder
ROOT_PATH = Path(__file__).parent 

def resize(event):
    global window_width, window_height
    if event.widget.widgetName == "toplevel":
        if (window_width != event.width) and (window_height != event.height):
            window_width, window_height = event.width,event.height
            print(f"The width of Toplevel is {window_width} and the height of Toplevel "
                  f"is {window_height}")

window_width, window_height = 0, 0

if __name__ == '__main__': 
    root = tk.Tk()
    root.resizable(True, True)
    top = tk.Toplevel()
    root.bind("<Configure>", resize)
    tk.mainloop()


