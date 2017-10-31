import tkinter
from lesson4.program1.cursor import Cursor
from lesson4.program1.matplotlibobject import MatplotlibObject
from lesson4.program1.scalebutton import ScaleButton
from lesson4.program1.tabs import Tabs

if __name__ == "__main__":
    root = tkinter.Tk()

    mo = MatplotlibObject(root)
    cursor = Cursor(mo, 'spyAxes')
    scb1 = ScaleButton(root, mo, "-")
    scb2 = ScaleButton(root, mo, "+")
    tabs = Tabs(root, mo)

    tabs.setN("3")
    #sun, moon, earth
    tabs.setM("1.98892e30 7.34767309e22 597.2e22")
    tabs.setR("0 0 0 -1499.84467e8 0 -1.496e11")
    tabs.setV("0 0 30805 0 29.783e3 0")
    mo.scaleAxes(1.5e9)

    cursor.setTabs(tabs)

    root.mainloop()