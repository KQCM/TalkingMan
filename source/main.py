import tkinter as tk
from page import Page
from barchart_page import BarChart
from result_page import Result

# STATE = 

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        barchart = BarChart(self)
        result = Result(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        barchart.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        result.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=result.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=barchart.show)
        b3 = tk.Button(buttonframe, text="Add data", command=lambda: barchart.add_data(100))

        # b1.pack(side="left")
        # b2.pack(side="left")
        # b3.pack(side="left")

        barchart.change_label("This is the Bar Chart page!")

        barchart.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Talking Man")
    # root.attributes("-fullscreen", True)
    root.wm_geometry("400x400")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
