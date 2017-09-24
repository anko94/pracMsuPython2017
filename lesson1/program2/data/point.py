class Point:

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.mark = 0
