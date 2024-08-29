import tkinter as tk
    
class Namecard(tk.Frame): 
    def __init__(self, parent, height=0, width=0, window_width=100): 
        self.name_str = 'Student'
        self.from_str = 'Affiliation'

        self.tk = parent
        self._w = tk.Canvas(parent, bg='black', height=height, width=width, highlightthickness=0)

        self.char_name = tk.Label(
            self._w, justify='left', font=('Noto Sans', 50), 
            text=self.name_str, fg='#fefefe', bg='black', highlightthickness=0
        )

        self.from_name = tk.Label(
            self._w, justify='left', font=('Noto Sans', 40),
            text=self.from_str, fg='#aaddff', pady=5, bg='black', highlightthickness=0
        )

        self.rightpad = tk.Canvas(height=height, width=width, bg='black', highlightthickness=0)
        self.pad = tk.Canvas(self._w, height=height, width=5, bg='black', highlightthickness=0)

        self.line = tk.Canvas(parent, width=window_width, height=2, bg='#dddddd', highlightthickness=0)
        
        self.char_name.grid(column=0, row=0, sticky='sw')
        self.pad.grid(column=1, row=0)
        self.from_name.grid(column=2, row=0, sticky='sw')
        self.rightpad.grid(column=3, row=0)
        self.line.grid(row=1)
        self.configure(bg='black')

if __name__ == '__main__': 
    active_speaker = None # coming soon with: char sprite update! 
    tester = tk.Tk()
    tester.config(bg='black')
    tester.wm_attributes('-transparentcolor', 'black')
    #backdrop = NamecardBackdrop(tester, height=100, width=100)
    #backdrop.grid(column=0, row=0)

    namecard = Namecard(tester, height=100, width=200, window_width=500)
    namecard.grid(column=0, row=0)
    #tk.Widget.tkraise(aboveThis=backdrop)

    tester.mainloop()