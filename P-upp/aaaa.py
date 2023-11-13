import tkinter as tk

class ValueEntryPopup:
    def __init__(self, master):
        self.master = master
        self.master.title("Enter Value")

        self.label = tk.Label(self.master, text="Enter a value:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.ok_button = tk.Button(self.master, text="OK", command=self.get_value)
        self.ok_button.pack(pady=10)

    def get_value(self):
        user_input = self.entry.get()
        print("User entered:", user_input)
        self.master.destroy()

# Create an instance of the ValueEntryPopup class
root = tk.Tk()
popup = ValueEntryPopup(root)

# Start the main event loop
root.mainloop()




"""class Popup:
    def __init__(self) -> None:
        self.popup = tk.Tk()
        self.popup.geometry("400x600")
        self.feedback_var = tk.StringVar(value="Ange storlek på spelplanen")
        self.size_input = tk.Entry(self.popup)
        self.size_input.grid(row=2, column= 1)
        self.feedback_label = tk.Label(self.popup, textvariable=self.feedback_var)
        self.feedback_label.grid(row=1, column= 1)
        self.ok = tk.Button(self.popup, text="Ok", command= self.get_size)
        self.ok.grid(row=3, column= 1)
        self.popup.mainloop()
    
    def get_size(self):
        try:
            size = int(self.size_input.get())
        except:
            self.feedback_var.set("Värdet måste vara en int")
        else:
            if size < 4:
                self.feedback_var.set("Planen måste minst vara 4x4")
            else: 
                GameApp(size)
                self.popup.destroy()
                """


