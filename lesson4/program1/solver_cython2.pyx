from libc.math cimport sqrt
from cython.parallel cimport parallel, prange
from numpy cimport ndarray as ar
import cython

# without typed memoryview and with openmp
@cython.boundscheck(False)
def solver(int n, double G, double dt, ar[double] m, ar[double] t, ar[double] x, ar[double] y, ar[double] vx, ar[double] vy, ar[double] axm, ar[double] aym):
    cdef int i, j, f
    cdef double ax, ay
    cdef int nt = len(t)
    with nogil, parallel(num_threads=n):
        for j in prange(n, schedule='dynamic'):
            ax = 0
            ay = 0
            for f in range(n):
                if f != j:
                    ax = ax + m[f] * G * (x[f] - x[j]) / sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
                    ay = ay + m[f] * G * (y[f] - y[j]) / sqrt((x[f] - x[j])**2 + (y[f] - y[j])**2) ** 3
            axm[j] = ax
            aym[j] = ay
    for i in range(nt):
         if i != 0:
            with nogil, parallel(num_threads=n):
                for j in prange(n, schedule='dynamic'):
                    x[i * n + j] = x[(i - 1) * n + j] + vx[(i - 1) * n + j]*dt + 1.0/2*axm[(i-1)*n+j]*dt**2
                    y[i * n + j] = y[(i - 1) * n + j] + vy[(i - 1) * n + j] * dt + 1.0 / 2 * aym[(i - 1) * n + j] * dt ** 2
            with nogil, parallel(num_threads=n):
                for j in prange(n, schedule='dynamic'):
                    ax = 0
                    ay = 0
                    for f in range(n):
                        if f != j:
                            ax = ax + m[f] * G * (x[i * n + f] - x[i * n + j]) / sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
                            ay = ay + m[f] * G * (y[i * n + f] - y[i * n + j]) / sqrt((x[i * n + f] - x[i * n + j])**2 + (y[i * n + f] - y[i * n + j])**2) ** 3
                    axm[i * n + j] = ax
                    aym[i * n + j] = ay
                    vx[i * n + j] = vx[(i - 1) * n + j] + 1.0 / 2 * dt * (axm[i * n + j] + axm[(i - 1) * n + j])
                    vy[i * n + j] = vy[(i - 1) * n + j] + 1.0 / 2 * dt * (aym[i * n + j] + aym[(i - 1) * n + j])
    return x, y, vx, vy, axm, aym