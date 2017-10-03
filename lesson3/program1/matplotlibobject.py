import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy

class MatplotlibObject():

    def __init__(self, parent):

        f = Figure(figsize=(10, 10), dpi=200)
        a = f.add_subplot(111, xlim=-100, xbound=100, ylim=-100, ybound=100)

        X = numpy.linspace(-100, 100, endpoint = True)
        Y = numpy.sin(X)
        a.plot(X, Y)

        canvas = FigureCanvasTkAgg(f, parent)
        canvas.show()
        canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)