import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Tutorial")

label = tk.Label(root, text="Hello World", font = ("Arial", 40))
label.pack(padx=20, pady=20)

# tbox = tk.Text(root, height=10, font=("Arial", 20))
# tbox.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=3)
# buttonframe.columnconfigure(2, weight=1)
buttonframe.rowconfigure(0, weight=10)
buttonframe.rowconfigure(1, weight=5)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 20))
btn1.grid(row=0, column=0, sticky="news")

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 20))
btn2.grid(row=0, column=1, sticky="news")

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 20))
btn3.grid(row=1, column=0, sticky="news")

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 20))
btn4.grid(row=1, column=1, sticky="news")

buttonframe.pack(fill="both")

root.mainloop()