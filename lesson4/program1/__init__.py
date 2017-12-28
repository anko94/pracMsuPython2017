import tkinter
from lesson4.program1.cursor import Cursor
from lesson4.program1.matplotlibobject import MatplotlibObject
from lesson4.program1.scalebutton import ScaleButton
from lesson4.program1.tabs import Tabs
import random


def set3(tabs, mo):
    tabs.setN("3")
    # sun, moon, earth
    tabs.setM("1.98892e30 7.34767309e22 597.2e22")
    tabs.setR("0 0 0 -1499.84467e8 0 -1.496e11")
    tabs.setV("0 0 30805 0 29.783e3 0")
    mo.scaleAxes(1.5e9)


def set10(tabs, mo):
    tabs.setN("5")
    # sun, mer, moon, earth
    tabs.setM("1.98892e30 3.33022e23 4.8685e24 7.34767309e22 597.2e22")
    tabs.setR("0 0 0 -57909176e3 0 -108000000e3 0 -1499.84467e8 0 -1.496e11")
    tabs.setV("0 0 47870 0 35020 0 30805 0 29.783e3 0")
    mo.scaleAxes(1.5e9)


def setN(tabs, mo, N):
    tabs.setN(str(N))
    m = ""
    r = ""
    v = ""
    n = 1000
    k = n/N
    f = -1
    for i in range(N):
        f*=-1
        m = m + str(random.uniform(3e10, 3e12))
        r = r + str(f*(k*i+1)) + " " + str(random.uniform(-1000, 1000))
        v = v + str(random.uniform(-1, 1)) + " " + str(random.uniform(-1, 1))
        if i != N-1:
            m += " "
            r += " "
            v += " "
    tabs.setM(m)
    tabs.setR(r)
    tabs.setV(v)
    mo.scaleAxes(30)


if __name__ == "__main__":
    root = tkinter.Tk()

    mo = MatplotlibObject(root)
    cursor = Cursor(mo, 'spyAxes')
    scb1 = ScaleButton(root, mo, "-")
    scb2 = ScaleButton(root, mo, "+")
    tabs = Tabs(root, mo)

    # set3(tabs, mo)
    # set10(tabs, mo)
    setN(tabs, mo, 10)

    cursor.setTabs(tabs)

    root.mainloop()