import tkinter
from lesson3.program1.cursor import Cursor
from lesson3.program1.matplotlibobject import MatplotlibObject
from lesson3.program1.scalebutton import ScaleButton
from lesson3.program1.tabs import Tabs

if __name__ == "__main__":

    root = tkinter.Tk()

    mo = MatplotlibObject(root)
    cursor = Cursor(mo, 'spyAxes')
    scb1 = ScaleButton(root, mo, "-")
    scb2 = ScaleButton(root, mo, "+")
    tabs = Tabs(root)
    cursor.setTabs(tabs)

    root.mainloop()