import tkinter as tk

def make_canvas(root, bg, h, w): 
    return tk.Canvas(root, bg=bg, height=h, width=w)

if __name__ == '__main__': 
    test_root = tk.Tk() 
    make_canvas(test_root, '#ff0000', 100, 100)
    test_root.mainloop() 