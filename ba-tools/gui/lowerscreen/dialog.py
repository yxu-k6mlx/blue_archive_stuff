import tkinter as tk
from PIL import Image, ImageTk

class DialogBackdrop(tk.Frame): 
    def __init__(self, root, bg_image_path=''): 
        self.tk = root
        self._w = tk.Canvas(root, width=1200, height=900, highlightthickness=0)

        self.bdimg = Image.open('blue_archive_stuff/ba-tools/assets/ui/DialogDisplay/text_backdrop.png')
        self.bdimg = self.bdimg.resize((1025, 400), Image.Resampling.LANCZOS)
        self.tkbd = ImageTk.PhotoImage(self.bdimg)

        self.bgimg = Image.open(bg_image_path)
        self.bgimg.resize((1200, 900), Image.Resampling.LANCZOS)
        self.tkbg = ImageTk.PhotoImage(self.bgimg)
        
        self._w.create_image(500, 900/2, image=self.tkbg)
        self._w.create_image(500, 900/2+185, image=self.tkbd)


class DialogText(tk.Frame): 
    def __init__(self, root, line0='', line1='', line2='', textsize=30): 
        self.tk = root 
        self._w = tk.Canvas(root, width=1200, height=400, bg='purple', highlightthickness=0)

        self.y_offset = 1000

        self.line0 = tk.Label(self._w, text=line0, font=('Noto Sans SemiBold', textsize), fg='#fefefe', bg='black', padx=0, pady=0, justify='left')
        self.line1 = tk.Label(self._w, text=line1, font=('Noto Sans SemiBold', textsize), fg='#fefefe', bg='black', padx=0, pady=0, justify='left')
        self.line2 = tk.Label(self._w, text=line2, font=('Noto Sans SemiBold', textsize), fg='#fefefe', bg='black', padx=0, pady=0, justify='left')

        self.line0.grid(column=0, row=0, sticky='sw')
        self.line1.grid(column=0, row=1, sticky='sw')
        self.line2.grid(column=0, row=2, sticky='sw')
        

if __name__ == '__main__': 
    test = tk.Tk()
    test.title('DialogBackdrop Test')
    backdrop = DialogBackdrop(test, bg_image_path='blue_archive_stuff/ba-tools/assets/data/Background/BG_HQ.jpg')
    text = DialogText(test, line0='Line0', line1='Line1', line2='Line 2')
    text.place(x=0, y=0)
    test.resizable(True, True)
    test.mainloop()
    