import tkinter as tk
from PIL import Image, ImageTk

class DialogBackdrop(tk.Frame): 
    def __init__(self, root, bg_image_path=''): 
        self.tk = root
        self._w = tk.Canvas(root, width=1200, height=900)

        self.bdimg = Image.open('blue_archive_stuff/ba-tools/assets/ui/DialogDisplay/text_backdrop.png')
        self.bdimg = self.bdimg.resize((1025, 400), Image.Resampling.LANCZOS)
        self.tkbd = ImageTk.PhotoImage(self.bdimg)

        self.bgimg = Image.open(bg_image_path)
        self.bgimg.resize((1200, 900), Image.Resampling.LANCZOS)
        self.tkbg = ImageTk.PhotoImage(self.bgimg)
        
        self._w.create_image(1200/2, 900/2, image=self.tkbg)
        self._w.create_image(1200/2, 900/2+185, image=self.tkbd)

if __name__ == '__main__': 
    test = tk.Tk()
    test.title('DialogBackdrop Test')
    backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
    test.resizable(True, True)
    test.mainloop()
    