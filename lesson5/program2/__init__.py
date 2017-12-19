import multiprocessing as mp
import time
from random import randint


def work(A, B, I, J, C, columns):
    for i in range(len(I)):
        A1 = getRowI(A, I[i])
        for j in range(len(J)):
            B1 = getColumnJ(B, J[j])
            a = 0
            for k in range(len(B1)):
                a += A1[k]*B1[k]
            C[I[i] * columns + J[j]] = a


def getRowI(A, i):
    A1 = []
    for j in range(len(A[0])):
        A1.append(A[i][j])
    return A1


def getColumnJ(B, j):
    B1 = []
    for i in range(len(B)):
        B1.append(B[i][j])
    return B1


if __name__ == "__main__":
    A = []
    B = []
    for i in range(200):
        E = []
        E1 = []
        for j in range(200):
            E.append(randint(-j, j))
            E1.append(randint(-j, j))
        A.append(E)
        B.append(E1)

    cResult = []
    for i in range(len(A)):
        C1 = []
        for j in range(len(B[0])):
            sum1 = 0
            for j1 in range(len(A[0])):
                sum1 += A[i][j1]*B[j1][j]
            C1.append(sum1)
        cResult.append(C1)

    C = mp.Array('d', range(len(A)*len(B[0])))
    start_time = time.time()
    columns = len(B[0])
    rows = len(A)
    if len(B) != len(A[0]):
        print("wrong matrices")
    else:
        proccessesAmount = 200
        processes = []
        addFields = 0
        num = int(rows*columns/proccessesAmount)
        if num != rows*columns/proccessesAmount:
            addFields = rows*columns - proccessesAmount*num
        count = 0
        f = 0
        I = []
        J = []
        for i in range(len(A)):
            I.append(i)
            for j in range(len(B[0])):
                J.append(j)
                count += 1
                if count == num:
                    f+=1
                    process = mp.Process(target=work, args=(A, B, I, J, C, columns))
                    processes.append(process)
                    process.start()
                    I = []
                    if j != len(B[0]) - 1:
                        I.append(i)
                    J = []
                    count = 0
            if addFields != 0 and i == len(A)-1 and f == proccessesAmount:
                process = mp.Process(target=work, args=(A, B, I, J, C, columns))
                processes.append(process)
                process.start()
        for t in processes:
            t.join()
        Cresult = []
        for i in range(len(A)):
            C1 = []
            for j in range(len(B[0])):
                C1.append(C[i*columns+j])
            Cresult.append(C1)
        # print(Cresult)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    for i in range(len(Cresult)):
        for j in range(len(Cresult[0])):
            if Cresult[i][j] != cResult[i][j]:
                print("false")

