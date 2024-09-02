import tkinter as tk
from lowerscreen.dialog import DialogBackdrop, DialogText
from lowerscreen.namecard import Namecard
from middlescreen.display import DispArea

import platform

class SceneDisp(tk.Frame): 
    def __init__(self, root, w_limit=1200, h_limit=900): 
        self.tk = root
        self._w = tk.Canvas(root, width=w_limit, height=h_limit, bg=None)
        self.backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
        self.namecard = Namecard(test, height=100, width=200, window_width=500, namesize=40, orgsize=35)
        self.dialog = DialogText(test, line0='這是第一行字 0 1 2 3 4 5 6', line1='This is line 2', line2='0 1 2 3 4 5 6 7 8 9 10 11 12', textsize=35)
        
        self.disp_area = DispArea(test, v_limit=1000, h_limit=800)
        self.tkchar = self.disp_area.parsechar('yukka')
        self.disp_area.dispchar(self.tkchar)

        self.backdrop.place(x=0, y=-75)
        self.disp_area.place(x=400, y=75)
        self.namecard.place(x=0, y=425)
        self.dialog.place(x=0, y=525)
        self.dialog.lift()

if __name__ == '__main__': 
    test = tk.Tk()
    test.geometry('1010x750')
    scene = SceneDisp(test, w_limit=1010, h_limit=750)
    
    tk.mainloop()

    """
    backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
    namecard = Namecard(test, height=100, width=200, window_width=500)
    dialog = DialogText(test, line0='這是第一行字', line1='This is line 2', line2='0 1 2 3 4 5 6 7 8 9 10 11 12')
    
    backdrop.place(x=0, y=0)
    namecard.place(x=100, y=480)
    dialog.place(x=100, y=580)
    
    tk.mainloop()
    """