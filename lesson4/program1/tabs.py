from tkinter import ttk
import tkinter
from tkinter.colorchooser import *
import xml.etree.cElementTree as et
import scipy.integrate
import numpy as np
import threading


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

    def saveFile(self):
        root = et.Element("root")
        axes = et.SubElement(root, "axes")
        xlim = et.SubElement(axes, "xlim")
        xmax = et.SubElement(axes, "xmax")
        ylim = et.SubElement(axes, "ylim")
        ymax = et.SubElement(axes, "ymax")
        currentAxes = self.mo.getCurrentAxes()
        xlim.text = str(currentAxes[0][0])
        xmax.text = str(currentAxes[0][1])
        ylim.text = str(currentAxes[1][0])
        ymax.text = str(currentAxes[1][1])
        color = et.SubElement(root, "color")
        r = et.SubElement(color, "r")
        g = et.SubElement(color, "g")
        b = et.SubElement(color, "b")
        c = (0, 0, 0)
        if self.color[0] != 0:
            c = (self.color[0][0] / 255, self.color[0][1] / 255, self.color[0][2] / 255)
        r.text = str(c[0])
        g.text = str(c[1])
        b.text = str(c[2])
        slider = et.SubElement(root, "slider")
        slider.text = str(self.w.get())
        circles = et.SubElement(root, "circles")
        circleList = self.mo.getCircleList()
        if len(circleList) != 0:
            for i in range(len(circleList)):
                circle = circleList[i]
                cir = et.SubElement(circles, "circle")
                x = et.SubElement(cir, "x")
                x.text = str(circle[0][0])
                y = et.SubElement(cir, "y")
                y.text = str(circle[0][1])
                radius = et.SubElement(cir, "radius")
                radius.text = str(circle[1])
                rcircle = et.SubElement(cir, "r")
                rcircle.text = str(circle[2][0])
                gcircle = et.SubElement(cir, "g")
                gcircle.text = str(circle[2][1])
                bcircle = et.SubElement(cir, "b")
                bcircle.text = str(circle[2][2])
        tree = et.ElementTree(root)
        tree.write(self.savefiledialog.get(1.0, tkinter.END)+".xml")

    def loadFile(self):
        tree = et.parse(self.openfiledialog.get(1.0, tkinter.END)+'.xml')
        root = tree.getroot()
        xlim = float(root[0][0].text)
        xmax = float(root[0][1].text)
        ylim = float(root[0][2].text)
        ymax = float(root[0][3].text)
        color = (float(root[1][0].text), float(root[1][1].text), float(root[1][2].text))
        self.defaultColor = (int(color[0]*255), int(color[1]*255), int(color[2]*255))
        slider = float(root[2].text)
        circles = root.find('circles')
        circleList = []
        for circle in circles.findall('circle'):
            circleList.append(((float(circle[0].text), float(circle[1].text)), float(circle[2].text), (float(circle[3].text), float(circle[4].text), float(circle[5].text))))
        self.w.set(slider)
        self.mo.loadFromXml((xlim, xmax, ylim, ymax), circleList)

    def verlet(self):
        #for example: x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, self.text6.get(1.0, tkinter.END).split(" "))),
                    list(map(float, self.text7.get(1.0, tkinter.END).split(" ")))], [])
        m = list(map(float, self.text5.get(1.0, tkinter.END).split(" ")))
        n = int(self.text4.get(1.0, tkinter.END))
        G = 6.674
        t = np.linspace(0, 20, 20)
        dt = 20/20
        x = []
        y = []
        for i in range(n):
            x.append(init[i*2])
            y.append(init[i*2+1])
        vx = []
        vy = []
        for i in range(n):
            vx.append(init[i*2+2*n])
            vy.append(init[i*2+1+2*n])
        axm = []
        aym = []
        for j in range(n):
            ax = 0
            ay = 0
            for f in range(n):
                if f != j:
                    if x[f] != x[j]:
                        ax += m[f] * G * (x[f] - x[j]) / abs(x[f] - x[j]) ** 3
                    else:
                        ax += 0
                    if y[f] != y[j]:
                        ay += m[f] * G * (y[f] - y[j]) / abs(y[f] - y[j]) ** 3
                    else:
                        ay += 0
            axm.append(ax)
            aym.append(ay)
        for i in range(len(t)):
            if i != 0:
                for j in range(n):
                    x.append(x[(i-1)*n+j] + vx[(i-1)*n+j]*dt + 1.0/2*axm[(i-1)*n+j]*dt**2)
                    y.append(y[(i - 1) * n + j] + vy[(i - 1) * n + j] * dt + 1.0 / 2 * aym[(i - 1) * n + j] * dt ** 2)
                for j in range(n):
                    ax = 0
                    ay = 0
                    for f in range(n):
                        if f != j:
                            if x[i * n + f] != x[i * n + j]:
                                ax += m[f] * G * (x[i * n + f] - x[i * n + j]) / abs(
                                    x[i * n + f] - x[i * n + j]) ** 3
                            else:
                                ax += 0
                            if y[i * n + f] != y[i * n + j]:
                                ay += m[f] * G * (y[i * n + f] - y[i * n + j]) / abs(
                                    y[i * n + f] - y[i * n + j]) ** 3
                            else:
                                ay += 0
                    axm.append(ax)
                    aym.append(ay)
                    vx.append(vx[(i - 1) * n + j] + 1.0 / 2 * dt * (axm[i * n + j] + axm[(i - 1) * n + j]))
                    vy.append(vy[(i - 1) * n + j] + 1.0 / 2 * dt * (aym[i * n + j] + aym[(i - 1) * n + j]))
        print(len(x), x)
        print(len(y), y)
        print(len(vx), vx)
        print(len(vy), vy)
        print(len(axm), axm)
        print(len(aym), aym)
        self.drawCircles(x, y, n)

    def drawCircles(self, x, y, n):
        c = 1/(n*2)
        for i in range(int(len(x)/n)):
            color = 0
            for j in range(n):
                color += c
                self.mo.drawCircle((x[i*n+j], y[i*n+j]), 1, (color,color,color))

    def scipySolve(self, init, x, n, m):
        G = 6.674
        x0 = []
        y0 = []
        for i in range(n):
            x0.append(init[i*2])
            y0.append(init[i * 2 + 1])
        vx0 = []
        vy0 = []
        for i in range(n):
            vx0.append(init[i*2 + n])
            vy0.append(init[i * 2 + 1 + n])
        result = []
        for i in range(n):
            result.append(vx0[i])
            result.append(vy0[i])
            sumx = 0
            sumy = 0
            for k in range(n-1):
                if k != i:
                    sumx += G * m[k] * (x0[k] - x0[i])/abs((x0[k] - x0[i])**3)
                    sumy += G * m[k] * (y0[k] - y0[i]) / abs((y0[k] - y0[i]) ** 3)
            result.append(sumx)
            result.append(sumy)
        return result


    def scipy(self):
        # for example: m1, m2, m3, x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, self.text6.get(1.0, tkinter.END).split(" "))), list(map(float, self.text7.get(1.0, tkinter.END).split(" ")))], [])
        t = np.linspace(0, 3, 100)
        n = int(self.text4.get(1.0, tkinter.END))
        result = scipy.integrate.odeint(self.scipySolve, init, t, args=(n,
                                                                        list(map(float,
                                                                                 self.text5.get(1.0, tkinter.END).split(" ")))))
        x = []
        y = []
        for i in range(len(result)):
            for j in range(n):
                x.append(result[i][j*2])
                y.append(result[i][j * 2 + 1])
        self.drawCircles(x, y, n)

    class MyThread(threading.Thread):
        def __init__(self, n, j, m, G, x, axm, y, aym):
            threading.Thread.__init__(self)
            self.n = n
            self.j = j
            self.m = m
            self.G = G
            self.x = x
            self.axm = axm
            self.y = y
            self.aym = aym

        def run(self):
            ax = 0
            ay = 0
            for f in range(self.n):
                if f != self.j:
                    ax += self.m[f] * self.G * (self.x[f] - self.x[self.j]) / abs(self.x[f] - self.x[self.j]) ** 3
                    ay += self.m[f] * self.G * (self.y[f] - self.y[self.j]) / abs(self.y[f] - self.y[self.j]) ** 3
            self.axm.insert(self.j, ax)
            self.aym.insert(self.j, ay)

    class MyThread2(threading.Thread):
        def __init__(self, n, i, j, dt, G, x, vx, axm, y, vy, aym):
            threading.Thread.__init__(self)
            self.n = n
            self.i = i
            self.j = j
            self.dt = dt
            self.G = G
            self.vx = vx
            self.x = x
            self.axm = axm
            self.vy = vy
            self.y = y
            self.aym = aym

        def run(self):
            self.x.insert(self.i * self.n + self.j, self.x[(self.i - 1) * self.n + self.j] +
                          self.vx[(self.i - 1) * self.n + self.j] * self.dt + 1.0 / 2 * self.axm[(self.i - 1) * self.n + self.j] * self.dt ** 2)
            self.y.insert(self.i * self.n + self.j, self.y[(self.i - 1) * self.n + self.j] +
                          self.vy[(self.i - 1) * self.n + self.j] * self.dt + 1.0 / 2 * self.aym[
                              (self.i - 1) * self.n + self.j] * self.dt ** 2)

    class MyThread3(threading.Thread):
        def __init__(self, n, i, j, dt, G, x, vx, m, axm, y, vy, aym):
            threading.Thread.__init__(self)
            self.n = n
            self.i = i
            self.j = j
            self.dt = dt
            self.G = G
            self.vx = vx
            self.x = x
            self.m = m
            self.axm = axm
            self.y = y
            self.vy = vy
            self.aym = aym

        def run(self):
            ax = 0
            ay = 0
            for f in range(self.n):
                if f != self.j:
                    ax += self.m[f] * self.G * (self.x[self.i * self.n + f] - self.x[self.i * self.n + self.j]) / abs(
                        self.x[self.i * self.n + f] - self.x[self.i * self.n + self.j]) ** 3
                    ay += self.m[f] * self.G * (self.y[self.i * self.n + f] - self.y[self.i * self.n + self.j]) / abs(
                        self.y[self.i * self.n + f] - self.y[self.i * self.n + self.j]) ** 3
            self.axm.insert(self.i * self.n + self.j, ax)
            self.aym.insert(self.i * self.n + self.j, ay)
            self.vx.append(self.vx[(self.i - 1) * self.n + self.j] + 1.0 / 2 * self.dt * (self.axm[self.i * self.n + self.j] + self.axm[(self.i - 1) * self.n + self.j]))
            self.vy.append(self.vy[(self.i - 1) * self.n + self.j] + 1.0 / 2 * self.dt * (self.aym[self.i * self.n + self.j] + self.aym[(self.i - 1) * self.n + self.j]))

    def verletThreading(self):
        # for example: x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, self.text6.get(1.0, tkinter.END).split(" "))),
                    list(map(float, self.text7.get(1.0, tkinter.END).split(" ")))], [])
        m = list(map(float, self.text5.get(1.0, tkinter.END).split(" ")))
        n = int(self.text4.get(1.0, tkinter.END))
        G = 6.674
        t = np.linspace(0, 3, 100)
        dt = 3.0 / 100
        x = [] * n * 100
        y = [] * n * 100
        for i in range(n):
            x.append(init[i*2])
            y.append(init[i*2+1])
        vx = [] * n * 100
        vy = [] * n * 100
        for i in range(n):
            vx.append(init[i*2 + 2*n])
            vy.append(init[i * 2 + 1 + 2 * n])
        axm = [] * n * 100
        aym = [] * n * 100
        threads = []
        for j in range(n):
            thread = self.MyThread(n, j, m, G, x, axm, y, aym)
            thread.start()
            threads.append(thread)
        for thr in threads:
            thr.join()
        for i in range(len(t)):
            if i != 0:
                threads = []
                for j in range(n):
                    thread = self.MyThread2(n, i, j, dt, G, x, vx, axm, y, vy, aym)
                    threads.append(thread)
                    thread.start()
                for thr in threads:
                    thr.join()
                threads = []
                for j in range(n):
                    thread = self.MyThread3(n, i, j, dt, G, x, vx, m, axm, y, vy, aym)
                    threads.append(thread)
                    thread.start()
                for thr in threads:
                    thr.join()
        print(len(x), x)
        print(len(y), y)
        print(len(vx), vx)
        print(len(vy), vy)
        print(len(axm), axm)
        print(len(aym), aym)
        self.drawCircles(x, y, n)

    def verletMultipricessing(self):
        print("verlet-multiprocessing")

    def verletCython(self):
        print("verlet-cython")

    def verletOpencl(self):
        print("verlet-opencl")

    def __init__(self, root, mo):
        style = ttk.Style()
        self.mo = mo
        style.configure("TNotebook.Tab", background='gray', foreground="black", font=1)
        nb = ttk.Notebook(root)
        page1 = ttk.Frame(nb, height=150, width=50)
        self.text1 = tkinter.Text(page1, height=1, width=50)
        self.text1.pack()
        self.text2 = tkinter.Text(page1, height=1, width=50)
        self.text2.pack()
        self.defaultColor = (0, 0, 0)
        self.color = (0, 0, 0)

        #color
        def getColor():
            color = askcolor(self.defaultColor)
            self.color = color
            if color[0] is not None:
                self.defaultColor = (int(color[0][0]), int(color[0][1]), int(color[0][2]))

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

        #radiobuttons
        page2 = ttk.Frame(nb)
        self.chooseRadiobutton = -1
        MODES = [
            ("scipy", "1"),
            ("verlet", "2"),
            ("verlet-threading", "3"),
            ("verlet-multiprocessing", "4"),
            ("verlet-cython", "5"),
            ("verlet-opencl", "6")
        ]
        options = {1: self.scipy,
                   2: self.verlet,
                   3: self.verletThreading,
                   4: self.verletMultipricessing,
                   5: self.verletCython,
                   6: self.verletOpencl,
        }
        v = tkinter.StringVar()
        v.set("L")  # initialize
        for text, mode in MODES:
            def command(mode=mode, text=text):
                self.chooseRadiobutton = mode
                options[int(mode)]()
            b = tkinter.Radiobutton(page2, text=text,
                            variable=v, value=mode, command=command)
            b.pack(anchor=tkinter.W)

        self.text4 = tkinter.Text(page2, height=1, width=20)
        self.text4.pack()
        self.text5 = tkinter.Text(page2, height=1, width=20)
        self.text5.pack()
        self.text6 = tkinter.Text(page2, height=1, width=20)
        self.text6.pack()
        self.text7 = tkinter.Text(page2, height=1, width=20)
        self.text7.pack()

        # xml-file
        page3 = ttk.Frame(nb)
        self.savefiledialog = tkinter.Text(page3, height=1, width=50)
        self.savefiledialog.pack()
        tkinter.Button(page3, text='save file', command=self.saveFile).pack()
        self.openfiledialog = tkinter.Text(page3, height=1, width=50)
        self.openfiledialog.pack()
        tkinter.Button(page3, text='load file', command=self.loadFile).pack()

        nb.add(page1, text='Edit')
        nb.add(page2, text='Model')
        nb.add(page3, text='Load/Save')
        nb.pack(side='left')
