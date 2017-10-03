import tkinter
from lesson3.program1.matplotlibobject import MatplotlibObject


def helloCallBack1():
    mo.scaleAxes(1.5)
    print(1)


def helloCallBack2():
    print(2)


if __name__ == "__main__":

    root = tkinter.Tk()

    mo = MatplotlibObject(root)

    a = tkinter.Button(root, text="+", command=helloCallBack1)
    a.pack()

    b = tkinter.Button(root, text="-", command=helloCallBack2)
    b.pack()

    root.mainloop()