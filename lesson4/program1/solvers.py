import math
import tkinter
import numpy as np
import scipy.integrate
import threading
import multiprocessing as mp


class Solvers:
    def verlet(self, nStr, mStr, xyStr, vStr):
        #for example: x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, xyStr)),
                    list(map(float, vStr))], [])
        m = list(map(float, mStr))
        n = int(nStr)
        G = 6.674e-11
        T = 10000000
        Tn = 100
        t = np.linspace(0, T, Tn)
        dt = T/Tn
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
                    ax += m[f] * G * (x[f] - x[j]) / math.sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
                    ay += m[f] * G * (y[f] - y[j]) / math.sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
            axm.append(ax)
            aym.append(ay)
        for i in range(len(t)):
            if i != 0:
                for j in range(n):
                    x.append(x[(i - 1) * n + j] + vx[(i - 1) * n + j]*dt + 1.0/2*axm[(i-1)*n+j]*dt**2)
                    y.append(y[(i - 1) * n + j] + vy[(i - 1) * n + j] * dt + 1.0 / 2 * aym[(i - 1) * n + j] * dt ** 2)
                for j in range(n):
                    ax = 0
                    ay = 0
                    for f in range(n):
                        if f != j:
                            ax += m[f] * G * (x[i * n + f] - x[i * n + j]) /\
                                  math.sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
                            ay += m[f] * G * (y[i * n + f] - y[i * n + j]) /\
                                  math.sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
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
        self.countError(nStr, mStr, xyStr, vStr, x, y, n)
        return x, y, n

    def scipySolve(self, init, t, n, m):
        G = 6.674e-11
        x0 = []
        y0 = []
        for i in range(n):
            x0.append(init[i*2])
            y0.append(init[i * 2 + 1])
        vx0 = []
        vy0 = []
        for i in range(n):
            vx0.append(init[i*2 + 2*n])
            vy0.append(init[i * 2 + 1 + 2*n])
        result = []
        for i in range(n):
            result.append(vx0[i])
            result.append(vy0[i])
        for i in range(n):
            sumx = 0
            sumy = 0
            for k in range(n):
                if k != i:
                    sumx += G * m[k] * (x0[k] - x0[i]) / math.sqrt((x0[k] - x0[i])**2 + (y0[k] - y0[i])**2) ** 3
                    sumy += G * m[k] * (y0[k] - y0[i]) / math.sqrt((x0[k] - x0[i])**2 + (y0[k] - y0[i])**2) ** 3
            result.append(sumx)
            result.append(sumy)
        return result

    def scipy(self, nStr, mStr, xyStr, vStr):
        # for example: m1, m2, m3, x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, xyStr)), list(map(float, vStr))], [])
        T = 10000000
        Tn = 100
        t = np.linspace(0, T, Tn)
        n = int(nStr)
        result = scipy.integrate.odeint(self.scipySolve, init, t, args=(n,
                                                                        list(map(float,
                                                                                 mStr))))
        x = []
        vx = []
        vy = []
        y = []
        for i in range(len(result)):
            for j in range(n):
                x.append(result[i][j*2])
                y.append(result[i][j * 2+1])
                vx.append(result[i][j * 2+2*n])
                vy.append(result[i][j * 2+1+2*n])
        print(x)
        print(y)
        print(vx)
        print(vy)
        return x, y, n

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
                    ax += self.m[f] * self.G * (self.x[f] - self.x[self.j]) /\
                          math.sqrt((self.x[f] - self.x[self.j])**2 + (self.y[f] - self.y[self.j])**2) ** 3
                    ay += self.m[f] * self.G * (self.y[f] - self.y[self.j]) /\
                          math.sqrt((self.x[f] - self.x[self.j])**2 + (self.y[f] - self.y[self.j])**2) ** 3
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
                    ax += self.m[f] * self.G * (self.x[self.i * self.n + f] - self.x[self.i * self.n + self.j]) / \
                          math.sqrt((self.x[self.i * self.n + f] - self.x[self.i * self.n + self.j])**2 + (self.y[self.i * self.n + f] - self.y[self.i * self.n + self.j])**2) ** 3
                    ay += self.m[f] * self.G * (self.y[self.i * self.n + f] - self.y[self.i * self.n + self.j]) /\
                          math.sqrt((self.x[self.i * self.n + f] - self.x[self.i * self.n + self.j])**2 + (self.y[self.i * self.n + f] - self.y[self.i * self.n + self.j])**2) ** 3
            self.axm.insert(self.i * self.n + self.j, ax)
            self.aym.insert(self.i * self.n + self.j, ay)
            self.vx.append(self.vx[(self.i - 1) * self.n + self.j] + 1.0 / 2 * self.dt * (self.axm[self.i * self.n + self.j] + self.axm[(self.i - 1) * self.n + self.j]))
            self.vy.append(self.vy[(self.i - 1) * self.n + self.j] + 1.0 / 2 * self.dt * (self.aym[self.i * self.n + self.j] + self.aym[(self.i - 1) * self.n + self.j]))

    def verletThreading(self, nStr, mStr, xyStr, vStr):
        # for example: x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, xyStr)),
                    list(map(float, vStr))], [])
        m = list(map(float, mStr))
        n = int(nStr)
        G = 6.674e-11
        T = 10000000
        Tn = 100
        t = np.linspace(0, T, Tn)
        dt = T / Tn
        x = [] * n * 100
        y = [] * n * 100
        for i in range(n):
            x.append(init[i * 2])
            y.append(init[i * 2 + 1])
        vx = [] * n * 100
        vy = [] * n * 100
        for i in range(n):
            vx.append(init[i * 2 + 2 * n])
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
        self.countError(nStr, mStr, xyStr, vStr, x, y, n)
        return x, y, n

    def verletMultiprocessing(self, nStr, mStr, xyStr, vStr):
        def work1(n, j, m, G, x, axm, y, aym):
            ax = 0
            ay = 0
            for f in range(n):
                if f != j:
                    ax += m[f] * G * (x[f] - x[j]) / math.sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
                    ay += m[f] * G * (y[f] - y[j]) / math.sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
            axm[j] = ax
            aym[j] = ay

        def work2(n, i, j, dt, G, x, vx, axm, y, vy, aym):
            x[i * n + j] = x[(i - 1) * n + j] + vx[(i - 1) * n + j] * dt + 1.0 / 2 * axm[(i - 1) * n + j] * dt ** 2
            y[i * n + j] = y[(i - 1) * n + j] + vy[(i - 1) * n + j] * dt + 1.0 / 2 * aym[(i - 1) * n + j] * dt ** 2

        def work3(n, i, j, dt, G, x, vx, m, axm, y, vy, aym):
            ax = 0
            ay = 0
            for f in range(n):
                if f != j:
                    ax += m[f] * G * (x[i * n + f] - x[i * n + j]) / \
                          math.sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
                    ay += m[f] * G * (y[i * n + f] - y[i * n + j]) / \
                          math.sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
            axm[i * n + j] = ax
            aym[i * n + j] = ay
            vx[i * n + j] = (vx[(i - 1) * n + j] + 1.0 / 2 * dt * (
                axm[i * n + j] + axm[(i - 1) * n + j]))
            vy[i * n + j] = (vy[(i - 1) * n + j] + 1.0 / 2 * dt * (
                aym[i * n + j] + aym[(i - 1) * n + j]))

        # for example: x1(0), y1(0), x2(0), y2(0), x3(0), y3(0), vx1(0), vy1(0), vx2(0), vy2(0), vx3(0), vy3(0)
        init = sum([list(map(float, xyStr)),
                    list(map(float, vStr))], [])
        m = list(map(float, mStr))
        n = int(nStr)
        G = 6.674e-11
        T = 10000000
        Tn = 100
        t = np.linspace(0, T, Tn)
        dt = T / Tn
        x = mp.Array('d', range(n * 100))
        y = mp.Array('d', range(n * 100))
        for i in range(n):
            x[i] = init[i * 2]
            y[i] = init[i * 2 + 1]
        vx = mp.Array('d', range(n * 100))
        vy = mp.Array('d', range(n * 100))
        for i in range(n):
            vx[i] = init[i * 2 + 2 * n]
            vy[i] = init[i * 2 + 1 + 2 * n]
        axm = mp.Array('d', range(n * 100))
        aym = mp.Array('d', range(n * 100))
        processes = []
        for j in range(n):
            process = mp.Process(target=work1, args=(n, j, m, G, x, axm, y, aym))
            process.start()
            processes.append(process)
        for thr in processes:
            thr.join()
        for i in range(len(t)):
            if i != 0:
                processes = []
                for j in range(n):
                    process = mp.Process(target=work2, args=(n, i, j, dt, G, x, vx, axm, y, vy, aym))
                    processes.append(process)
                    process.start()
                for thr in processes:
                    thr.join()
                processes = []
                for j in range(n):
                    process = mp.Process(target=work3, args=(n, i, j, dt, G, x, vx, m, axm, y, vy, aym))
                    processes.append(process)
                    process.start()
                for thr in processes:
                    thr.join()
        x1 = []
        for i in range(len(x)):
            x1.append(x[i])
        y1 = []
        for i in range(len(y)):
            y1.append(y[i])
        vx1 = []
        for i in range(len(vx)):
            vx1.append(vx[i])
        vy1 = []
        for i in range(len(vy)):
            vy1.append(vy[i])
        axm1 = []
        for i in range(len(axm)):
            axm1.append(axm[i])
        aym1 = []
        for i in range(len(aym)):
            aym1.append(aym[i])
        print(len(x1), x1)
        print(len(y1), y1)
        print(len(vx1), vx1)
        print(len(vy1), vy1)
        print(len(axm1), axm1)
        print(len(aym1), aym1)
        self.countError(nStr, mStr, xyStr, vStr, x1, y1, n)
        return x1, y1, n

    def verletCython(self, nStr, mStr, xyStr, vStr):
        print("verlet-cython")

    def verletOpencl(self, nStr, mStr, xyStr, vStr):
        print("verlet-opencl")

    def countError(self, nStr, mStr, xyStr, vStr, x, y, n):
        xScipy, yScipy, nScipy = self.scipy(nStr, mStr, xyStr, vStr)
        sum = 0
        for i in range(len(x)):
            sum += ((x[i] - xScipy[i])**2 + (y[i] - xScipy[i])**2)
        sum = sum / ((len(x)-1)**2)
        sum = math.sqrt(sum)
        print("Error:", sum)


