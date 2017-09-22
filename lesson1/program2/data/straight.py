from lesson1.program2.data.point import Point
from lesson1.program2.data.vector import Vector

# (x-x0)/m=(y-y0)/n=(z-z0)/k, a=(m,n,k)
class Straight:

    def __init__(self, point1: Point, point2: Point):
        self.a = Vector(point2.x - point1.x, point2.y - point1.y, point2.z - point1.z)
        self.point0 = point1
        self.point2 = point2

    # 1 if point on the straight, 0 - otherwise
    def isPointOnTheStraight(self, point3: Point):
        eq1 = (point3.x-self.point0.x)/self.a.m
        eq2 = (point3.y-self.point0.y)/self.a.n
        eq3 = (point3.z-self.point0.z)/self.a.k
        if eq1 != eq2 or eq2 != eq3 or eq1 != eq3 :
            return 0
        return 1