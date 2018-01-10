from scipy.integrate import odeint
from scipy.optimize import fsolve
import numpy as np
import math


tFlag = 0
T0 = []


def scipySolve(T0, t, e, c, lambda12, lambda23, lambda34,
                      lambda45, S, S12, S23, S34, S45, c0):
    return [1/c[0]*(-e[0]*S[0]*c0*(T0[0]/100)**4-lambda12*S12*(T0[0]-T0[1])),
            1/c[1]*(-e[1] * S[1] * c0 * (T0[1] / 100) ** 4 - lambda12 * S12 * (T0[1] - T0[0]) - lambda23 * S23 * (T0[1] - T0[2])),
            1/c[2]*(-e[2] * S[2] * c0 * (T0[2] / 100) ** 4 - lambda23 * S23 * (T0[2] - T0[1]) - lambda34 * S34 * (T0[2] - T0[3])),
            1/c[3]*(-e[3] * S[3] * c0 * (T0[3] / 100) ** 4 - lambda34 * S34 * (T0[3] - T0[2]) - lambda45 * S45 * (T0[3] - T0[4])),
            1/c[4]*(-e[4] * S[4] * c0 * (T0[4] / 100) ** 4 - lambda45 * S45 * (T0[4] - T0[3]) + (20 + 3*math.sin(t/4)))]


def equation(T, e, lambda12, lambda23, lambda34,
                lambda45, S, S12, S23, S34, S45, c0, Tmin):
    T1, T2, T3, T4, T5 = T
    return (e[0]*S[0]*c0*(T1/100)**4+lambda12*S12*(T1-T2),
            e[1] * S[1] * c0 * (T2 / 100) ** 4 + lambda12 * S12 * (T2 - T1) + lambda23 * S23 * (T2 - T3),
            e[2] * S[2] * c0 * (T3 / 100) ** 4 + lambda23 * S23 * (T3 - T2) + lambda34 * S34 * (T3 - T4),
            e[3] * S[3] * c0 * (T4 / 100) ** 4 + lambda34 * S34 * (T4 - T3) + lambda45 * S45 * (T4 - T5),
            e[4] * S[4] * c0 * (T5 / 100) ** 4 + lambda45 * S45 * (T5 - T4) - (20 + 3*math.sin(Tmin/4)))


def scipy(Tmin, Tmax, Tn):
    t = np.linspace(Tmin, Tmax, Tn)
    e = [0.1, 0.1, 0.05, 0.02, 0.05]
    c = [900, 900, 520, 1930, 520]
    lambda12 = 240
    lambda23 = 130
    lambda34 = 118
    lambda45 = 10.5
    S12 = 4*math.pi
    S23 = 4*math.pi
    S34 = math.pi
    S45 = math.pi
    S1 = math.pi*(5+3.0/5*math.sqrt(17)) - S12
    S2 = 32 * math.pi - S12 - S23
    S3 = 268 - S23 - S34
    S4 = 4*math.pi - S34 - S45
    S5 = 218.207296 - S45
    S = [S1, S2, S3, S4, S5]
    c0 = 5.67
    global tFlag, T0
    if tFlag == 0:
        # T10, T20, T30, T40, T50 = fsolve(equation, (100.11,100.11,100.11,100.11,100.11), args=(e, lambda12, lambda23, lambda34,
        #                                     lambda45, S, S12, S23, S34, S45, c0, Tmin))
        # T0 = [T10, T20, T30, T40, T50]
        T0 = [100, 100, 0, 0, 0]
    result = odeint(scipySolve, T0, t, args=(e, c, lambda12,
                                             lambda23, lambda34, lambda45,
                                             S, S12, S23, S34, S45, c0))
    if tFlag == 0:
        tFlag = 1
    else:
        T0 = [result[Tn-1][0], result[Tn-1][1], result[Tn-1][2], result[Tn-1][3], result[Tn-1][4]]
    return result


def findMax(mas):
    n1 = len(mas)
    n2 = len(mas[0])
    max = mas[0][0]
    for i in range(0, n1):
        for j in range(0, n2):
            if mas[i][j] > max:
                max = mas[i][j]
    return max


def findMin(mas):
    n1 = len(mas)
    n2 = len(mas[0])
    min = mas[0][0]
    for i in range(0, n1):
        for j in range(0, n2):
            if mas[i][j] < min:
                min = mas[i][j]
    return min


def getResult(tmin, tmax, n, nt):
    result = []
    result1 = []
    d = (tmax-tmin)/n
    t=tmin
    for i in range(n):
        result.append(scipy(t,t+d,nt))
        t+=d
    for i in range(len(result)):
        for j in range(len(result[0])):
            result1.append(result[i][j])
    return result1


if __name__ == "__main__":
    mas = getResult(0,1,10,10)
    print(findMin(mas), findMax(mas))
    print(mas)