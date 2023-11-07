import tkinter as tk

class InputGUI:
    def __init__(self) -> None:
        self.window = tk.Tk()
        
        for i in range(5):
            for j in range(5):
                self.name_l = tk.Label(self.window, text = "Namme")
                self.name_l.grid(row=i, column=j)
        
        self.name = tk.Entry(self.window)
        self.name.grid(row=0,column=1)
        
        self.output = tk.Label(self.window)
        self.output.grid(row=1,column=0)
        self.ok = tk.Button(self.window, text="OK", command = self.update_output)
        self.ok.grid(row=0,column=2)
        self.window.mainloop()
        
        
    def update_output(self):
        self.output["text"] = f"Hej, {self.name.get()}"
        
a = InputGUI()