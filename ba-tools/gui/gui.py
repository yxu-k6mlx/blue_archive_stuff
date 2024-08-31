import tkinter as tk
from lowerscreen.dialog import DialogBackdrop, DialogText
from lowerscreen.namecard import Namecard

class SceneDisp(tk.Frame): 
    def __init__(self, root, w_limit=1200, h_limit=900): 
        self.tk = root
        self._w = tk.Canvas(root, width=w_limit, height=h_limit)
        self.backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
        self.namecard = Namecard(test, height=100, width=200, window_width=500)
        self.dialog = DialogText(test, line0='这是第一行字', line1='This is line 2', line2='0 1 2 3 4 5 6 7 8 9 10 11 12')
        
        self.backdrop.place(x=0, y=0)
        self.namecard.place(x=100, y=500)
        self.dialog.place(x=100, y=600)

if __name__ == '__main__': 
    test = tk.Tk()
    scene = SceneDisp(test)

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