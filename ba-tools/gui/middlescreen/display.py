import tkinter as tk

class DispArea(tk.Frame): 
    def __init__(self, root, v_limit=0, h_limit=0): 
        self.tk = root 
        self.width, self.height = self.calculate_position(v_limit=v_limit, h_limit=h_limit)

        self._w = tk.Canvas(root, width=self.width, height=self.height, bg='black') 
        
        self._w.grid(column=0,row=0)

    def text_to_disp(self, root, text): 
        self.text = text 
        self.label = tk.Label(root, text=self.text, fg='white', font=('Noto Sans', 50, 'bold'))

    def calculate_position(self, v_limit, h_limit): 
        v_ratio = 0.4
        return (1-v_ratio)*v_limit, h_limit

if __name__ == '__main__': 
    test = tk.Tk() 
    disp_area = DispArea(test, v_limit=1000, h_limit=200)
    
    test.mainloop()