import tkinter as tk
from gradient import GradientFrame
from PIL import Image, ImageTk

class DialogBackdrop(tk.Frame): 
    def __init__(self, root): 
        self.frame = tk.Canvas(root, width=1600, height=1200)
        self.image = ImageTk.PhotoImage(file='blue_archive_stuff/ba-tools/assets/ui/DialogDisplay/text_backdrop.png')
        self.image = ImageTk.PhotoImage(file='')
        self.frame.create_image(0, 0, image=self.image)
        self.frame.pack() 

if __name__ == '__main__': 
    test = tk.Tk()
    test.title('DialogBackdrop Test')
    backdrop = DialogBackdrop(test)
    test.resizable(True, True)
    test.mainloop()
    