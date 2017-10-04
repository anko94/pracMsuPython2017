import tkinter
import numpy
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class MatplotlibObject():

    def scaleAxes(self, scale):
        xlim = self.axes.get_xlim()
        ylim = self.axes.get_ylim()
        self.axes.clear()
        self.axes.set_xlim(xlim[0] * scale, xlim[1] * scale)
        self.axes.set_ylim(ylim[0] * scale, ylim[1] * scale)
        X = numpy.linspace(xlim[0]*scale, xlim[1]*scale, endpoint=True)
        Y = numpy.sin(X)
        self.b = self.axes.plot(X, Y)
        self.canvas.show()

    def __init__(self, parent):
        self.figure = Figure(figsize=(10, 10), dpi=200)
        self.axes = self.figure.add_subplot(111, xlim=[-100, 100], ylim=[-100, 100])

        X = numpy.linspace(-100, 100, endpoint=True)
        Y = numpy.sin(X)
        self.b = self.axes.plot(X, Y)

        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
