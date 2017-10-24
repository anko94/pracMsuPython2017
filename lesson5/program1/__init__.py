import threading


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
    A = [[1, 2, 3, 5], [3, 3, 4, 5], [1, 2 ,1, 5], [3, 4, 5, 3]]
    B = [[1, 1], [3, 3], [4, 4], [3, 4]]
    C = []
    for i in range(len(A)):
        E = [0] * len(B[0])
        C.append(E)
    if len(B) != len(A[0]):
        print("wrong matrices")
    else:
        threads = []
        k = 0
        for i in range(len(B)):
            A1 = A[i]
            if k >= len(B[0]):
                k = 0
            B1 = []
            for j in range(len(B)):
                B1.append(B[j][k])
            thread = MyThread(A1, B1, i, k, C)
            threads.append(thread)
            thread.start()
            k += 1
        for t in threads:
            t.join()
        print(C)
