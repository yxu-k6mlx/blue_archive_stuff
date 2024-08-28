import tkinter as tk

class Namecard(tk.Frame): 
    def __init__(self, parent, height=0, width=0, x=0, y=0): 
        self.name_str = 'Student'
        self.from_str = 'Affiliation'
        self.tk = parent
        self._w = tk.Canvas(
            parent, height=height, width=width
        )
        self.char_name = tk.Label(
            self._w, justify='left', font=('Noto Sans', 50), 
            text=self.name_str, fg='white'
        )

        self.from_name = tk.Label(
            self._w, justify='left', font=('Noto Sans', 40), 
            text=self.from_str, fg='#aaddff', pady=5
        )
        
        self.pad = tk.Canvas(self._w, height=50, width=5)

        self.char_name.grid(column=0, row=0, sticky='sw')
        self.pad.grid(column=1, row=0)
        self.from_name.grid(column=2, row=0, sticky='sw')

if __name__ == '__main__': 
    active_speaker = None # coming soon with: char sprite update! 
    tester = tk.Tk()
    namecard = Namecard(tester, height=100, width=900)
    namecard.place(x=0, y=0)
    tester.mainloop()