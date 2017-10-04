import tkinter
from lesson3.program1.matplotlibobject import MatplotlibObject
from lesson3.program1.scalebutton import ScaleButton
from lesson3.program1.tabs import Tabs

if __name__ == "__main__":

    root = tkinter.Tk()

    mo = MatplotlibObject(root)
    scb1 = ScaleButton(root, mo, "-")
    scb1 = ScaleButton(root, mo, "+")
    tabs = Tabs(root)

    root.mainloop()