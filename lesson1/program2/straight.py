from lesson1.program2.point import Point
from lesson1.program2.vector import Vector

# (x-x0)/m=(y-y0)/n=(z-z0)/k, a=(m,n,k)
class Straight:
    def __int__(self, point1: Point, point2: Point):
        self.a = Vector(point2.x - point1.x, point2.y - point1.y, point2.z - point1.z)
        self.point = point1