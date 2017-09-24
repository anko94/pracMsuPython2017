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
        if self.a.m!=0:
            eq1 = (point3.x-self.point0.x)/self.a.m
        else:
            eq1 = point3.x-self.point0.x
        if self.a.n!=0:
            eq2 = (point3.y-self.point0.y)/self.a.n
        else:
            eq2 = point3.y-self.point0.y
        if self.a.k!=0:
            eq3 = (point3.z-self.point0.z)/self.a.k
        else:
            eq3 = point3.z-self.point0.z
        if eq1 == eq2 and eq2 == eq3 or self.a.m == 0 and eq1==0 and eq2 == eq3 or self.a.n==0 and eq2==0 and eq1==eq3 \
                or self.a.k==0 and eq3==0 and eq2==eq1 or self.a.m==0 and self.a.n==0 and eq2==0 and eq1==0 or \
                                         self.a.m==0 and self.a.k==0 and eq1==0 and eq3==0 or self.a.n==0 and self.a.k==0 and eq2==0 and eq3==0:
            return 1
        return 0