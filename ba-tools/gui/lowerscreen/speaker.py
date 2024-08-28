import tkinter as tk

class Namecard(tk.Frame): 
    def __init__(self, parent, height=0, width=0, x=0, y=0): 
        self.char_name = ''
        self.org_name = ''
        self.tk = parent
        self._w = tk.Canvas(
            parent, height=height, width=width
        )

    def set_charname(self, char_name : str) -> None: 
        self.char_name = char_name 
        print(f'Character name set to {char_name}')
    
    def get_charname(self) -> str: 
        return self.char_name
    
    def set_orgname(self, org_name : str) -> None: 
        self.org_name = org_name

    def get_orgname(self): 
        return self.org_name
    
    def disp(self) -> bool: 
        
        return False


if __name__ == '__main__': 
    pass