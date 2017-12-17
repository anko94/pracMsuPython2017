import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.integrate
import numpy as nm


def getXcYc(x, k1m, k3, k3m, k2, n):
    k1 = [0.0] * n
    y = [0.0] * n
    z = [0.0] * n
    alk = math.sqrt(k3) / (math.sqrt(k3m) + math.sqrt(k3))
    for i in range(n):
        y[i] = (1 - x[i]) * alk
        z[i] = 1 - x[i] - y[i]
        k1[i] = (k1m*x[i]+k2*z[i]**2*x[i])/(z[i])

    i = 0
    DI = [0.0] * 1000
    yh = []
    xh = []
    k1h = []
    ysn = []
    xsn = []
    k1sn = []
    ydi = []
    xdi = []
    k1di = []
    k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
    a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
    a12 = -k1[i] + 2 * k2 * x[i] * z[i]
    a21 = -2 * k3 * z[i]
    a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
    sp[i] = a11 + a22
    det[i] = a11 * a22 - a12 * a21
    DI[i] = sp[i] ** 2 - 4 * det[i]
    for i in range(1, n):
        k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a12 = -k1[i] + 2 * k2 * x[i] * z[i]
        a21 = -2 * k3 * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        sp[i] = a11 + a22
        det[i] = a11 * a22 - a12 * a21
        DI[i] = sp[i] ** 2 - 4 * det[i]
        if sp[i] * sp[i - 1] <= 0:
            x1 = x[i-1] - sp[i-1]*(x[i]-x[i-1])/(sp[i]-sp[i-1])
            y1 = (1-x1)*alk
            k11 = (k1m * x1 + k2 * (1-x1-y1) ** 2 * x1) / (1-x1-y1)
            yh.append(y1)
            xh.append(x1)
            k1h.append(k11)
        if det[i] * det[i - 1] <= 0:
            x1 = x[i - 1] - det[i - 1] * (x[i] - x[i - 1]) / (det[i] - det[i - 1])
            y1 = (1 - x1) * alk
            k11 = (k1m * x1 + k2 * (1 - x1 - y1) ** 2 * x1) / (1 - x1 - y1)
            ysn.append(y1)
            xsn.append(x1)
            k1sn.append(k11)
        if DI[i] * DI[i - 1] <= 0:
            x1 = x[i - 1] - DI[i - 1] * (x[i] - x[i - 1]) / (DI[i] - DI[i - 1])
            y1 = (1 - x1) * alk
            k11 = (k1m * x1 + k2 * (1 - x1 - y1) ** 2 * x1) / (1 - x1 - y1)
            ydi.append(y1)
            xdi.append(x1)
            k1di.append(k11)

    figure, axes = plt.subplots()
    plt.xlabel("k1")
    plt.ylabel("x,y")
    axes.plot(k1, x, 'r')
    axes.plot(k1, y, 'b')
    for i in range(len(xh)):
        axes.plot(k1h[i], xh[i], 'oy')
        axes.plot(k1h[i], yh[i], 'oy')
    for i in range(len(xsn)):
        axes.plot(k1sn[i], xsn[i], 'og')
        axes.plot(k1sn[i], ysn[i], 'og')
    plt.show()


def scipySolve(r, t, k1, k1m, k2, k3, k3m):
    return [k1*(1 - r[0] - r[1]) - k1m*r[0] - k2*(1-r[0]-r[1])**2*r[0],
            k3*(1-r[0]-r[1])**2 - k3m*r[1]**2]


if __name__ == "__main__":
    # двухпараметрический анализ на плоскости (k1,k1m)
    k2 = 1.05
    k3m = 0.002
    k3 = 0.0032
    alk = math.sqrt(k3) / (math.sqrt(k3m) + math.sqrt(k3))
    x = np.linspace(0, 0.999, 1000)
    n = len(x)
    y = [0.0]*1000
    z = [0.0]*1000
    k1 = [0.0]*1000
    k1m = [0.0]*1000
    sp = [0.0]*1000
    det = [0.0]*1000
    K1 = [0.0]*1000
    K1m = [0.0]*1000
    Sp = [0.0]*1000
    Det = [0.0]*1000

    # #зависимость от k1 для неск. значений параметра k1m
    # getXcYc(x, 0.001, k3, k3m, k2, n)
    # getXcYc(x, 0.005, k3, k3m, k2, n)
    # getXcYc(x, 0.01, k3, k3m, k2, n)
    # getXcYc(x, 0.015, k3, k3m, k2, n)
    # getXcYc(x, 0.02, k3, k3m, k2, n)
    #
    # # зависимость от k1 для неск. значений параметра k3m
    # getXcYc(x, 0.005, k3, 0.0005, k2, n)
    # getXcYc(x, 0.005, k3, 0.001, k2, n)
    # getXcYc(x, 0.005, k3, 0.002, k2, n)
    # getXcYc(x, 0.005, k3, 0.003, k2, n)
    # getXcYc(x, 0.005, k3, 0.004, k2, n)

    # расчет линии нейтральности
    for i in range(n):
        y[i] = (1 - x[i]) * alk
        z[i] = 1 - x[i] - y[i]
        k1m[i] = (-k2 * z[i] ** 2 * x[i] - k2 * z[i] ** 3 + 2 * k2 * x[i] * z[i] ** 2 - 2 * k3 * z[
            i] ** 2 - 2 * k3m * y[i] * z[i]) / (x[i] + z[i])
        k1[i] = (k1m[i] * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -k1[i] - k1m[i] - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a12 = -k1[i] + 2 * k2 * x[i] * z[i]
        a21 = -2 * k3 * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        det[i] = a11 * a22 - a12 * a21
        sp[i] = a11 + a22
        if det[i] <= 0:
            k1m[i] = -1

    # расчет линии кратности
    for i in range(n):
        K1m[i] = ((k2 * z[i] ** 2 * x[i] + k2 * z[i] ** 3 - 2 * k2 * x[i] * z[i]**2) * (
        2 * k3 * z[i] + 2 * k3m * y[i]) - (k2 * z[i] ** 2 * x[i] - 2 * k2 * x[i] * z[i] ** 2) * 2 * k3 * z[i]) / (
                   x[i] * 2 * k3 * z[i] - (x[i] + z[i]) * (2 * k3 * z[i] + 2 * k3m * y[i]))
        K1[i] = (K1m[i] * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -K1[i] - K1m[i] - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a12 = -K1[i] + 2 * k2 * x[i] * z[i]
        a21 = -2 * k3 * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        Det[i] = a11 * a22 - a12 * a21
        Sp[i] = a11 + a22

    # #построение фазового портрета
    # figure, axes = plt.subplots()
    # axes.set_title("Parametric Portrait")
    # plt.xlabel("km1")
    # plt.ylabel("k1")
    # axes.plot(k1m, k1, 'r')
    # axes.plot(K1m, K1, 'b')
    # plt.show()

    #odeint
    r = [0, 0]
    t = nm.linspace(0, 10000, 1000000)
    result = scipy.integrate.odeint(scipySolve, r, t, args=(0.119, 0.008, k2, k3, k3m))
    x11 = []
    y11 = []
    for i in range(len(result)):
        x11.append(result[i][0])
        y11.append(result[i][1])

    figure, axes = plt.subplots()
    plt.xlabel("x")
    plt.ylabel("y")
    axes.plot(x11, y11, 'r')
    plt.show()

    figure, axes = plt.subplots()
    axes.plot(t, x11, 'r')
    axes.plot(t, y11, 'b')
    plt.show()

    # построение фазового портрета
