from libc.math cimport sqrt
import numpy as np

# without typed memoryview and openmp
def solver(int n, double G, double dt, m, t, x, y, vx, vy, axm, aym):
    cdef int i, j, f
    cdef double ax, ay
    for j in range(n):
        ax = 0
        ay = 0
        for f in range(n):
            if f != j:
                ax += m[f] * G * (x[f] - x[j]) / sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
                ay += m[f] * G * (y[f] - y[j]) / sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
        axm[j] = ax
        aym[j] = ay
    for i in range(len(t)):
        if i != 0:
            for j in range(n):
                x[i * n + j] = x[(i - 1) * n + j] + vx[(i - 1) * n + j]*dt + 1.0/2*axm[(i-1)*n+j]*dt**2
                y[i * n + j] = y[(i - 1) * n + j] + vy[(i - 1) * n + j] * dt + 1.0 / 2 * aym[(i - 1) * n + j] * dt ** 2
            for j in range(n):
                ax = 0
                ay = 0
                for f in range(n):
                     if f != j:
                        ax += m[f] * G * (x[i * n + f] - x[i * n + j]) / sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
                        ay += m[f] * G * (y[i * n + f] - y[i * n + j]) / sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
                axm[i * n + j] = ax
                aym[i * n + j] = ay
                vx[i * n + j] = vx[(i - 1) * n + j] + 1.0 / 2 * dt * (axm[i * n + j] + axm[(i - 1) * n + j])
                vy[i * n + j] = vy[(i - 1) * n + j] + 1.0 / 2 * dt * (aym[i * n + j] + aym[(i - 1) * n + j])
    return x, y, vx, vy, axm, aym