from tkinter import ttk
import tkinter


class Tabs:
    def __init__(self, root):
        style = ttk.Style()
        style.configure("TNotebook.Tab", background='gray', foreground="black", font=1)#, height=12, padding=20,

        nb = ttk.Notebook(root)
        page1 = ttk.Frame(nb, height=150, width=50)
        text1 = tkinter.Text(page1, height=1, width=50)
        text1.pack()
        text2 = tkinter.Text(page1, height=1, width=50)
        text2.pack()
        page2 = ttk.Frame(nb)
        nb.add(page1, text='Edit')
        nb.add(page2, text='Model')
        nb.pack(side='left')
