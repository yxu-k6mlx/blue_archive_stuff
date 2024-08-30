import tkinter as tk
from lowerscreen.dialog import DialogBackdrop
from lowerscreen.namecard import Namecard

if __name__ == '__main__': 
    test = tk.Tk()
    backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
    namecard = Namecard(test, height=100, width=200, window_width=500)
    
    backdrop.pack()
    namecard.place(x=100, y=500)

    tk.mainloop()