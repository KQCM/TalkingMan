import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Hello World", font = ("Arial", 40))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=10, font=("Arial", 20))
        self.textbox.pack(padx=20, pady=20)

        self.textbox.bind("<KeyPress>", self.handle_keypress)

        self.check_state = tk.BooleanVar()

        self.check = tk.Checkbutton(self.root, text="Check me!", font=("Arial", 20), variable=self.check_state)
        self.check.pack(padx=20, pady=20)

        self.button = tk.Button(self.root, text="Click me!", font=("Arial", 20), command=self.on_button_click)
        self.button.pack(padx=20, pady=20)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def on_button_click(self):
        self.label["text"] = self.textbox.get("1.0", tk.END)
        if self.check_state.get() == 1:
            self.label["text"] = self.label["text"].upper()
        else:
            messagebox.showinfo("Info", "You didn't check the box!")


    def handle_keypress(self, event):
        print(event.keysym)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    gui = MyGUI()