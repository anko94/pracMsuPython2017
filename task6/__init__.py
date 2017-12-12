import matplotlib.pyplot as plt
import math
import numpy as np


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
    a11i = [0.0] * 1000
    a22i = [0.0] * 1000
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
    a11i[i] = a11
    a22i[i] = a22
    sp[i] = a11 + a22
    det[i] = a11 * a22 - a12 * a21
    DI[i] = sp[i] ** 2 - 4 * det[i]
    for i in range(1, n):
        k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a12 = -k1[i] + 2 * k2 * x[i] * z[i]
        a21 = -2 * k3 * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        a11i[i] = a11
        a22i[i] = a22
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
    # axes.plot(k1, y, 'b')
    for i in range(len(xh)):
        axes.plot(k1h[i], xh[i], 'oy')
        # axes.plot(k1h[i], yh[i], 'oy')
    for i in range(len(xsn)):
        axes.plot(k1sn[i], xsn[i], 'og')
        # axes.plot(k1sn[i], ysn[i], 'og')

    # # find dmax
    # dmax = 0
    # i1 = 0
    # for i in range(n):
    #     if a11i[i]*a22i[i]<0:
    #         if dmax<math.fabs(a11i[i])/math.fabs(a22i[i]):
    #             dmax = math.fabs(a11i[i])/math.fabs(a22i[i])
    #             i1 = i
    # print(dmax, k1[i1])

    # # find a11*a22<0
    # for i in range(1000):
    #     axes.plot(k1[i], a11i[i]*a22i[i], 'or')

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    k1m = 0.01
    k2 = 1.05
    k3m = 0.002
    k3 = 0.0032

    x = np.linspace(0, 0.999, 1000)
    n = len(x)
    sp = [0.0] * 1000
    det = [0.0] * 1000

    getXcYc(x, k1m, k3, k3m, k2, n)