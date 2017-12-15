import threading
import time
from random import randint


class MyThread(threading.Thread):
    def __init__(self, A, B, i, k, C):
        threading.Thread.__init__(self)
        self.A = A
        self.B = B
        self.C = C
        self.i = i
        self.k = k

    def run(self):
        a = 0
        for j in range(len(self.A)):
            a += self.A[j]*self.B[j]
        self.C[self.i][self.k] = a


if __name__ == "__main__":
    A = []
    B = []
    for i in range(50):
        E = []
        E1 = []
        for j in range(50):
            E.append(randint(-j-1, j+1))
            E1.append(randint(-j-1, j+1))
        A.append(E)
        B.append(E1)
    C = []

    cResult = []
    for i in range(len(A)):
        C1 = []
        for j in range(len(B[0])):
            sum1 = 0
            for j1 in range(len(A[0])):
                sum1 += A[i][j1] * B[j1][j]
            C1.append(sum1)
        cResult.append(C1)
    start_time = time.time()
    for i in range(len(A)):
        E = [0] * len(B[0])
        C.append(E)
    if len(B) != len(A[0]):
        print("wrong matrices")
    else:
        threads = []
        for i in range(len(A)):
            A1 = A[i]
            for j in range(len(B[0])):
                B1 = []
                for k in range(len(B)):
                    B1.append(B[k][j])
                thread = MyThread(A1, B1, i, j, C)
                threads.append(thread)
                thread.start()
        for t in threads:
            t.join()
        # print(C)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    for i in range(len(C)):
        for j in range(len(C[0])):
            if C[i][j] != cResult[i][j]:
                print("false ", C[i][j], cResult[i][j])
