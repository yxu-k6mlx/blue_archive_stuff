import tkinter as tk
from gradient import GradientFrame
from PIL import Image, ImageTk

class DialogBackdrop(tk.Frame): 
    def __init__(self, root): 
        self.canvas = tk.Canvas(root, width=1200, height=900)

        self.bdimg = Image.open('blue_archive_stuff/ba-tools/assets/ui/DialogDisplay/text_backdrop.png')
        self.bdimg = self.bdimg.resize((1000, 400), Image.Resampling.LANCZOS)
        self.tkbd = ImageTk.PhotoImage(self.bdimg)

        self.bgimg = Image.open('blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
        self.bgimg.resize((1200, 900), Image.Resampling.LANCZOS)
        self.tkbg = ImageTk.PhotoImage(self.bgimg)
        
        self.canvas.create_image(1200/2, 900/2, image=self.tkbg)
        self.canvas.create_image(1200/2, 900/2+200, image=self.tkbd)
        self.canvas.grid(column=0,row=0)

if __name__ == '__main__': 
    test = tk.Tk()
    test.title('DialogBackdrop Test')
    backdrop = DialogBackdrop(test)
    test.resizable(True, True)
    test.mainloop()
    