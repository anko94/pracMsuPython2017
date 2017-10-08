from tkinter import ttk
import tkinter
from tkinter.colorchooser import *


class Tabs:
    def setXY(self, x, y):
        self.text1.delete(1.0, tkinter.END)
        self.text2.delete(1.0, tkinter.END)
        self.text1.insert(tkinter.INSERT, x)
        self.text2.insert(tkinter.INSERT, y)

    def getColor(self):
        color = (0, 0, 0)
        if self.color[0] != 0:
            color = (self.color[0][0]/255, self.color[0][1]/255, self.color[0][2]/255)
        return color

    def getRadius(self):
        return self.w.get()

    def __init__(self, root):
        style = ttk.Style()
        style.configure("TNotebook.Tab", background='gray', foreground="black", font=1)#, height=12, padding=20,

        nb = ttk.Notebook(root)
        page1 = ttk.Frame(nb, height=150, width=50)
        self.text1 = tkinter.Text(page1, height=1, width=50)
        self.text1.pack()
        self.text2 = tkinter.Text(page1, height=1, width=50)
        self.text2.pack()

        self.color = (0, 0, 0)

        #color
        def getColor():
            color = askcolor()
            self.color = color

        tkinter.Button(page1, text='Select Color', command=getColor).pack(side='left')

        #slider
        def setText(value):
            self.text3.delete(1.0, tkinter.END)
            self.text3.insert(tkinter.INSERT, value)

        self.w = tkinter.Scale(page1, from_=1.0, to=100.0, orient=tkinter.HORIZONTAL, command=setText)
        self.w.pack(side='right')

        def setValue():
            self.w.set(self.text3.get(1.0, tkinter.END))
        tkinter.Button(page1, text='Set Slider', command=setValue).pack(side='right')

        self.text3 = tkinter.Text(page1, height=1, width=5)
        self.text3.pack(side='right')

        page2 = ttk.Frame(nb)
        nb.add(page1, text='Edit')
        nb.add(page2, text='Model')
        nb.pack(side='left')
