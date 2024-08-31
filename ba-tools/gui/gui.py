import tkinter as tk
from lowerscreen.dialog import DialogBackdrop, DialogText
from lowerscreen.namecard import Namecard

if __name__ == '__main__': 
    test = tk.Tk()
    backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
    namecard = Namecard(test, height=100, width=200, window_width=500)
    dialog = DialogText(test, line0='這是第一行字', line1='This is line 2', line2='0 1 2 3 4 5 6 7 8 9 10 11 12')
    
    backdrop.pack()
    namecard.place(x=100, y=480)
    dialog.place(x=100, y=580)
    
    tk.mainloop()