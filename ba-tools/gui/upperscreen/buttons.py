import tkinter as tk
import math

class Askew_Button(tk.Frame):
    """
        Control buttons in Blue Archive are askew with an angle 
        They are defined below with create polygon with four outer vertices A->B->C->D wrapped inside its own canvas
         A /-----/ B
          /     /
         /-----/
        D      C
        where B.x-A.x = C.x - D.x = width, D.y-A.y = C.y-D.y = height
        and such that B.x - C.x = x_offset = A.x - D.x
    
    """
    def __init__(self, root, x=0, y=0, text='', height=50, width=100, x_offset=2, padx=5, pady=5): 
        self.transparent = 'grey'
        self.tk = root
        self.x_offset = x_offset
        self._w = tk.Canvas(root, height=height+pady, width=width+x_offset+padx, bg=self.transparent, highlightthickness=0)

        self.width = width 
        self.height = height 

        self.Ax, self.Ay = x + x_offset + padx, y+pady
        self.Bx, self.By = self.Ax + self.width, self.Ay
        self.Cx, self.Cy = self.Bx - x_offset, self.Ay + self.height
        self.Dx, self.Dy = x + padx, y + self.height + pady

        print(f'ABCD: {self.Ax, self.Ay}, {self.Bx, self.By}, {self.Cx, self.Cy}, {self.Dx, self.Dy}')
        
        self._w.create_polygon(
            self.Ax, self.Ay, 
            self.Bx, self.By, 
            self.Cx, self.Cy, 
            self.Dx, self.Dy, 
            fill = '#f1f1f1'
        )

        self._w.create_text(
            (self.Bx-self.Dx)/2, (self.Dy-self.Ay)/2, 
            justify='center', text=text, font=('Noto Sans', math.floor(height/2-pady), 'bold italic'), 
            fill='#1111aa'
        )

        root.wm_attributes('-transparentcolor', self.transparent)

class ControlBar(tk.Frame): 
    def __init__(self, root, x=0, y=0, height=50, width=100, x_offset=2, padx=5, pady=5):
        self.tk = root 
        self._w = tk.Canvas(root, height=(height+pady), width=2*(width+x_offset+padx) + 100)
        auto = Askew_Button(test_root, x=0, y=0, height=100, width=300, x_offset=40, text='AUTO')
        menu = Askew_Button(test_root, x=0, y=0, height=100, width=300, x_offset=40, text='MENU')
        auto.grid(column=0, row=0)
        menu.grid(column=1, row=0)

# Component testing code: 
if __name__ == '__main__': 
    test_root = tk.Tk()
    test_button = ControlBar(test_root, x=0, y=0, height=100, width=300, x_offset=40)
    test_button.place(x=0, y=0)
    test_root.title('Component Tester')
    test_root.mainloop() 

