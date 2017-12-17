import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate


def drawParametricPortrait(k2, k3, k3m, n):
    alk = math.sqrt(k3) / (math.sqrt(k3m) + math.sqrt(k3))
    x = np.linspace(0, 0.999, n)
    y = [0.0] * n
    z = [0.0] * n
    K1 = [0.0] * n
    K1m = [0.0] * n
    Sp = [0.0] * n
    Det = [0.0] * n
    k1 = [0.0] * n
    k1m = [0.0] * n
    sp = [0.0] * n
    det = [0.0] * n

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
        K1m[i] = ((k2 * z[i] ** 2 * x[i] + k2 * z[i] ** 3 - 2 * k2 * x[i] * z[i] ** 2) * (
            2 * k3 * z[i] + 2 * k3m * y[i]) - (k2 * z[i] ** 2 * x[i] - 2 * k2 * x[i] * z[i] ** 2) * 2 * k3 * z[i]) / (
                     x[i] * 2 * k3 * z[i] - (x[i] + z[i]) * (2 * k3 * z[i] + 2 * k3m * y[i]))
        K1[i] = (K1m[i] * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -K1[i] - K1m[i] - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a12 = -K1[i] + 2 * k2 * x[i] * z[i]
        a21 = -2 * k3 * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        Det[i] = a11 * a22 - a12 * a21
        Sp[i] = a11 + a22

    # построение параметрического портрета
    figure, axes = plt.subplots()
    axes.set_title("Parametric Portrait")
    plt.xlabel("km1")
    plt.ylabel("k1")
    axes.plot(k1m, k1, 'r')
    axes.plot(K1m, K1, 'b')
    plt.grid(True)
    plt.show()


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
    j2 = 0
    j3 = 0
    a11i = [0.0] * n
    a22i = [0.0] * n
    yh = []
    xh = []
    k1h = []
    ys1 = []
    xs1 = []
    k1s1 = []
    ys2 = []
    xs2 = []
    k1s2 = []
    k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
    a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
    a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
    a11i[i] = a11
    a22i[i] = a22
    sp[i] = a11 + a22
    for i in range(1, n):
        k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        a11i[i] = a11
        a22i[i] = a22
        sp[i] = a11 + a22
        if sp[i] * sp[i - 1] <= 0:
            x1 = x[i-1] - sp[i-1]*(x[i]-x[i-1])/(sp[i]-sp[i-1])
            y1 = (1-x1)*alk
            k11 = (k1m * x1 + k2 * (1-x1-y1) ** 2 * x1) / (1-x1-y1)
            yh.append(y1)
            xh.append(x1)
            k1h.append(k11)
        if a11i[i]*a11i[i-1] <= 0:
            xs1.append(x[i])
            ys1.append(y[i])
            k1s1.append(k1[i])
            j2 += 1
        if a22i[i] * a22i[i - 1] <= 0:
            xs2.append(x[i])
            ys2.append(y[i])
            k1s2.append(k1[i])
            j3 += 1
    figure, axes = plt.subplots()
    # plt.xlabel("k1")
    # plt.ylabel("x,y")
    # axes.plot(k1, x, 'r')
    # axes.plot(k1, y, 'b')
    # for i in range(len(xh)):
    #     axes.plot(k1h[i], xh[i], 'oy')
    #     axes.plot(k1h[i], yh[i], 'oy')
    # for i in range(len(xs1)):
    #     axes.plot(k1s1[i], xs1[i], 'og')
    #     axes.plot(k1s1[i], ys1[i], 'og')
    # for i in range(len(xs2)):
    #     axes.plot(k1s2[i], xs2[i], 'og')
    #     axes.plot(k1s2[i], ys2[i], 'og')

    # # find a11*a22<0s

    # find dmax
    dmax = 0
    i1 = 0
    for i in range(n):
        if a11i[i]*a22i[i]<0 and a11i[i]+a22i[i]<0:
            if dmax<abs(a11i[i])/abs(a22i[i]):
                dmax = abs(a11i[i])/abs(a22i[i])
                i1 = i
    print(dmax, k1[i1])

    plt.grid(True)
    plt.show()


def drawT(k1m, k2, k3, k3m, n):
    x = np.linspace(0, 0.9, 1000)
    y = [0.0] * n
    z = [0.0] * n
    k1 = [0.0] * n
    k1s1 = 0.116
    B = [0.0] * n
    disk = [0.0] * n
    dks = [0.0] * n
    h1 = []
    h2 = []
    nn1 = []
    nn2 = []
    k1s = []
    k1f = []
    K1S = []
    XS = []
    YS = []
    A11S = []
    A22S = []
    SPS = []
    DETS = []
    D1 = 0.01
    D2 = 1
    DD = D1 * D2
    L = 50
    is1 = 0
    j4 = 0
    i = 0
    alk = math.sqrt(k3) / (math.sqrt(k3m) + math.sqrt(k3))
    y[i] = (1 - x[i]) * alk
    z[i] = 1 - x[i] - y[i]
    k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
    a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
    a12 = -k1[i] + 2 * k2 * x[i] * z[i]
    a21 = -2 * k3 * z[i]
    a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
    sp[i] = a11 + a22
    det[i] = a11 * a22 - a12 * a21
    B[i] = D1 * a22 + D2 * a11
    disk[i] = B[i] ** 2 - 4 * DD * det[i]
    dks[i] = k1[i] - k1s1
    if disk[i] >= 0 and B[i] + math.sqrt(disk[i]) >= 0 and B[i] - math.sqrt(disk[i]) >= 0:
        h1.append((B[i] + math.sqrt(disk[i])) / (2 * DD))
        h2.append((B[i] - math.sqrt(disk[i])) / (2 * DD))
        nn1.append(math.sqrt(h1[is1]) * L / math.pi)
        nn2.append(math.sqrt(h2[is1]) * L / math.pi)
        k1s.append(k1[i])
        is1 += 1
    for i in range(1, n):
        y[i] = (1 - x[i]) * alk
        z[i] = 1 - x[i] - y[i]
        k1[i] = (k1m * x[i] + k2 * z[i] ** 2 * x[i]) / (z[i])
        a11 = -k1[i] - k1m - k2 * z[i] ** 2 + 2 * k2 * x[i] * z[i]
        a12 = -k1[i] + 2 * k2 * x[i] * z[i]
        a21 = -2 * k3 * z[i]
        a22 = -2 * k3 * z[i] - 2 * k3m * y[i]
        sp[i] = a11 + a22
        det[i] = a11 * a22 - a12 * a21
        B[i] = D1 * a22 + D2 * a11
        disk[i] = B[i] ** 2 - 4 * DD * det[i]
        dks[i] = k1[i] - k1s1
        if disk[i] >= 0 and B[i] + math.sqrt(disk[i]) >= 0 and B[i] - math.sqrt(disk[i]) >= 0:
            h1.append((B[i] + math.sqrt(disk[i])) / (2 * DD))
            h2.append((B[i] - math.sqrt(disk[i])) / (2 * DD))
            nn1.append(math.sqrt(h1[is1]) * L / math.pi)
            nn2.append(math.sqrt(h2[is1]) * L / math.pi)
            k1s.append(k1[i])
            is1 += 1
        if dks[i] * dks[i - 1] <= 0:
            j4 += 1
            K1S.append(k1[i])
            XS.append(x[i])
            YS.append(y[i])
            A11S.append(a11)
            A22S.append(a22)
            SPS.append(sp[i])
            DETS.append(det[i])

    figure, axes = plt.subplots()

    # axes.set_title("Turing Bifurcation")
    # plt.xlabel("k1")
    # plt.ylabel("k^2")
    # axes.plot(k1s, h1, 'or')
    # axes.plot(k1s, h2, 'ob')

    j4 = 0
    k11 = K1S[j4]
    A11 = A11S[j4]
    A22 = A22S[j4]
    S_A = SPS[j4]
    delta_A = DETS[j4]
    h = np.linspace(0, 60, 6000)
    nn = [0.0] * len(h)
    S_B = [0.0] * len(h)
    delta_B = [0.0] * len(h)
    gam1 = [0.0] * len(h)
    gam2 = [0.0] * len(h)
    for i in range(len(h)):
        nn[i] = math.sqrt(h[i])*L/math.pi
        S_B[i] = S_A - h[i] * (D1+D2)
        delta_B[i] = delta_A - (A11*D2 + A22*D1) * h[i] + DD*h[i]**2
        d = S_B[i]**2-4*delta_B[i]
        if d < 0:
            d = 0
        gam1[i] = 0.5*(S_B[i]+math.sqrt(d))
        gam2[i] = 0.5 * (S_B[i] -math.sqrt(d))
    Dis = (A11*D2+A22*D1)**2 - 4*delta_A*D1*D2
    if Dis<0:
        Dis = 0
    h11 = ((A11*D2+A22*D1) + math.sqrt(Dis))/(2*DD)
    h22 = ((A11*D2+A22*D1) - math.sqrt(Dis))/(2*DD)
    nh1 = math.sqrt(h11)*L/math.pi
    nh2 = math.sqrt(h22)*L/math.pi
    # axes.set_title("Determinant of matrix B")
    # plt.xlabel("k^2")
    # plt.ylabel("delta_B")
    # axes.plot(h, delta_B, "r")
    # axes.plot(h11, 0, "ob")
    # axes.plot(h22, 0, "ob")
    # print(math.pi/math.sqrt(h11))

    # axes.set_title("Eigenvalues of matrix B")
    # plt.xlabel("n")
    # plt.ylabel("delta_B")
    # axes.plot(nn, gam1, "r")
    # axes.plot(nn, gam2, "r")
    # axes.plot(nh1, 0, "ob")
    # axes.plot(nh2, 0, "ob")

    # численное интегрирование:
    L=70

    # # неуст. гармоники
    print(L*math.sqrt(h11)/math.pi, L*math.sqrt(h22)/math.pi)

    xs = XS[j4]
    ys = YS[j4]
    nw = 10
    x = np.linspace(0, L, 500)
    dx = L/500
    t = np.linspace(0, 10, 200)
    y = []
    i1 = 0
    for i in range(1000):
        if i1%2 == 0:
            y.append(xs + 0.1*math.cos(math.pi*nw*x[i%500]/L))
        else:
            y.append(ys)
        i1+=1
    result = scipy.integrate.odeint(solve, y, t, args=(k11, k1m, k2, k3, k3m, D1, D2, dx))

    # print(len(result[0]))#1000
    # print(len(result))#200

    #y1
    axes.plot(x, result[199][::2], 'r')
    #y2
    axes.plot(x, result[100][1::2], 'b')

    plt.grid(True)
    plt.show()


def f1(y1, y2, k1, km1, k2):
    return k1*(1-y1-y2)-km1*y1-k2*y1*(1-y1-y2)**2


def f2(y1, y2, k3, km3):
    return k3*(1-y1-y2)**2 - km3*y2**2


def solve(y, t, k1, km1, k2, k3, k3m, D1, D2, dx):
    u = y[::2]
    v = y[1::2]
    dydt = np.empty_like(y)
    dudt = dydt[::2]
    dvdt = dydt[1::2]
    dudt[0] = f1(u[0], v[0], k1, km1, k2) + D1 * (-2.0 * u[0] + 2.0 * u[1]) / dx ** 2
    dudt[1:-1] = f1(u[1:-1], v[1:-1], k1, km1, k2) + D1 * np.diff(u, 2) / dx ** 2
    dudt[-1] = f1(u[-1], v[-1], k1, km1, k2) + D1 * (- 2.0 * u[-1] + 2.0 * u[-2]) / dx ** 2
    dvdt[0] = f2(u[0], v[0], k3, k3m) + D2 * (-2.0 * v[0] + 2.0 * v[1]) / dx ** 2
    dvdt[1:-1] = f2(u[1:-1], v[1:-1], k3, k3m) + D2 * np.diff(v, 2) / dx ** 2
    dvdt[-1] = f2(u[-1], v[-1], k3, k3m) + D2 * (-2.0 * v[-1] + 2.0 * v[-2]) / dx ** 2
    return dydt


if __name__ == "__main__":
    k1m = 0.008
    k2 = 1.05
    k3m = 0.002
    k3 = 0.0032
    x = np.linspace(0, 0.9, 1000)
    n = len(x)
    sp = [0.0] * 1000
    det = [0.0] * 1000

    # drawParametricPortrait(k2, k3, k3m, n)
    # getXcYc(x, k1m, k3, k3m, k2, n)

    drawT(k1m, k2, k3, k3m, n)