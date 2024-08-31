import tkinter as tk
from PIL import Image, ImageTk

class DispArea(tk.Frame): 
    def __init__(self, root, v_limit=0, h_limit=0, chars=[None]*5): 
        self.tk = root 
        self.width = v_limit
        self.height = h_limit
        self._w = tk.Canvas(root, width=250, height=700, bg='purple', highlightthickness=0)

    def parsechar(self, charname): 
        char = Image.open(f'blue_archive_stuff/ba-tools/assets/data/Sprites/{charname}.png')
        char = char.resize((400, 800), Image.Resampling.LANCZOS)
        tkchar = ImageTk.PhotoImage(char)
        return tkchar

    def dispchar(self, tkchar, position=2): 
        self._w.create_image(100, 400, image=tkchar)

if __name__ == '__main__': 
    test = tk.Tk() 
    disp_area = DispArea(test, v_limit=200, h_limit=400)
    tkchar = disp_area.parsechar('yukka')
    disp_area.dispchar(tkchar)
    disp_area.pack() 
    test.mainloop()