import tkinter as tk

class Askew_Button(tk.Frame):
    def __init__(self, parent, height=100, width=300, text=''): 
        self.tk = parent
        self._w = tk.Canvas(parent, background='#0000ff')
        self._w.create_polygon(
            20, 0, 120, 0, 100, 50, 0, 50, outline='red'
        )

if __name__ == '__main__': 
    test_root = tk.Tk()
    test_button = Askew_Button(test_root)
    test_button.place(x=10, y=10)
    test_root.title('Component Tester')
    test_root.mainloop() 

