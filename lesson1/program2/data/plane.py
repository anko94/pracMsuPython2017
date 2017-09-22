# A*x+B*y+C*Z+D = 0
from lesson1.program2.data.point import Point


class Plane:
    def tryPoint(self, point: Point ):
        return self.A*point.x+self.B*point.y+self.C*point.z+self.D

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
