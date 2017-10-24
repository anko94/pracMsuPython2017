import threading


class MyThread(threading.Thread):
    def __init__(self, n, j, m, G, r, am):
        threading.Thread.__init__(self)
        self.n = n
        self.j = j
        self.m = m
        self.G = G
        self.r = r
        self.am = am

    def run(self):
        a = 0
        for f in range(self.n):
            if f != self.j:
                a += self.m[f] * self.G * (self.r[f] - self.r[self.j]) / abs(self.r[f] - self.r[self.j]) ** 3
        self.am.insert(self.j, a)

if __name__ == "__main__":
