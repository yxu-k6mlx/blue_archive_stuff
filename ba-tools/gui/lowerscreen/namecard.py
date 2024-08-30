import tkinter as tk

NAME_SPLIT_WIDTH = 20
LABEL_BG = 'purple'

class Namecard(tk.Frame): 
    def __init__(self, root, height=0, width=0, window_width=10): 
        self.name_str = 'Student'
        self.from_str = 'Affiliation'
        self.bg = 'red'
        self.tk = root
        self._w = tk.Canvas(root, bg=LABEL_BG, height=height, width=width, highlightthickness=0)

        self.char_name = tk.Label(
            self._w, justify='left', font=('Noto Sans', 40), 
            text=self.name_str, fg='#fefefe', bg=LABEL_BG, highlightthickness=0
        )

        self.pad = tk.Canvas(self._w, height=height, width=NAME_SPLIT_WIDTH, bg=LABEL_BG, highlightthickness=0)

        self.from_name = tk.Label(
            self._w, justify='left', font=('Noto Sans', 30),
            text=self.from_str, fg='#aaddff', pady=5, bg=LABEL_BG, highlightthickness=0
        )

        #self.rightpad = tk.Canvas(height=height, width=width, bg='black', highlightthickness=0)
        

        self.line_length = window_width
        #self.line = tk.Canvas(root, width=self.line_length, height=2, bg='red', highlightthickness=0)
        
        self.set_to_disp()

    def set_to_disp(self): 
        self.char_name.grid(column=0, row=0, sticky='sw')
        self.pad.grid(column=1, row=0)
        self.from_name.grid(column=2, row=0, sticky='sw')
        #self.rightpad.grid(column=3, row=0, sticky='sw')
        #self.line.grid(row=1)
        self.configure(bg='purple')

if __name__ == '__main__': 
    active_speaker = None # coming soon with: char sprite update! 
    tester = tk.Tk()
    #backdrop = NamecardBackdrop(tester, height=100, width=100)
    #backdrop.grid(column=0, row=0)

    namecard = Namecard(tester, height=100, width=200, window_width=500)
    namecard.grid(column=0, row=0)
    #tk.Widget.tkraise(aboveThis=backdrop)

    tester.mainloop()