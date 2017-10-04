from tkinter import ttk


class Tabs:
    def __init__(self, root):
        style = ttk.Style()
        style.configure("TNotebook.Tab", background='gray', foreground="black", height=12, padding=20, font=1)

        nb = ttk.Notebook(root)
        page1 = ttk.Frame(nb)
        page2 = ttk.Frame(nb)
        nb.add(page1, text='Edit')
        nb.add(page2, text='Model')
        nb.pack(side='left')
