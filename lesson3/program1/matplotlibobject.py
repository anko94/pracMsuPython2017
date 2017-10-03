import tkinter
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy


class MatplotlibObject():

    def scaleAxes(self, scale):
        self.a = self.f.add_subplot(111, xlim=-100*scale, xbound=100*scale, ylim=-100*scale, ybound=100*scale)

    def __init__(self, parent):
        self.f = Figure(figsize=(10, 10), dpi=200)
        self.a = self.f.add_subplot(111, xlim=[-100, 100], ylim=[-100, 100])

        X = numpy.linspace(-100, 100, endpoint=True)
        Y = numpy.sin(X)
        self.a.plot(X, Y)

        self.canvas = FigureCanvasTkAgg(self.f, parent)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
