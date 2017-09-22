from lesson1.program2.data.straight import Straight
from lesson1.program2.data.plane import Plane
from lesson1.program2.data.point import Point
import math

from lesson1.program2.data.vector import Vector


class Algebra:
    def getPlane(self, point1: Point, point2: Point, point3: Point):
        A = (point2.y - point1.y)*(point3.z-point1.z)-(point2.z-point1.z)*(point3.y-point1.y)
        B = -((point2.x - point1.x)*(point3.z-point1.z)-(point2.z-point1.z)*(point3.x-point1.x))
        C = (point2.x - point1.x)*(point3.y-point1.y)-(point2.y-point1.y)*(point3.x-point1.x)
        D = -point1.x*A - point1.y*B - point1.z*C
        return Plane(A, B, C, D)

    # 0 - planes match
    # 1 - planes are parallel
    # 2 - planes intersect
    def planeRelationship(self, plane1: Plane, plane2: Plane):
        if plane2.A != 0 and plane2.B != 0 and plane2.C != 0 and plane2.D != 0 and plane1.A/plane2.A == plane1.B/plane2.B and plane1.B/plane2.B == plane1.C/plane2.C and plane1.C/plane2.C == plane1.D/plane2.D\
                or plane2.A == 0 and plane2.B == 0 and plane2.C == 0 and plane2.D == 0 and plane1.A == 0 and plane1.B == 0 and plane1.C == 0 and plane1.D == 0:
            return 0
        elif plane2.A != 0 and plane2.B != 0 and plane2.C != 0 and plane2.D != 0 and plane1.A/plane2.A == plane1.B/plane2.B and plane1.B/plane2.B == plane1.C/plane2.C and plane1.C/plane2.C != plane1.D/plane2.D\
                or plane2.A != 0 and plane2.B != 0 and plane2.C != 0 and plane2.D == 0 and plane1.A/plane2.A == plane1.B/plane2.B and plane1.B/plane2.B == plane1.C/plane2.C:
            return 1
        return 2

    # a11 a12
    # a21 a22
    def det2x2(self, a11, a12, a21, a22):
        return a11*a22 - a12*a21

    # t0m1 - s0m2 + x1 - x2 = 0
    # t0n1 - s0n2 + y1 - y2 = 0
    # t0k1 - s0k2 + z1 - z2 = 0
    # solve system of equations for straights that don't match and parallel
    def solveSystemOfEquations(self, straight1: Straight, straight2: Straight):
        a1 = straight1.a
        a2 = straight2.a
        point1 = straight1.point0
        point2 = straight2.point0
        t1 = 0
        s1 = 0
        t2 = 0
        s2 = 0
        t3 = 0
        s3 = 0
        A1 = self.det2x2(a1.m, -a2.m, a1.n, -a2.n)
        A2 = self.det2x2(a1.m, -a2.m, a1.k, -a2.k)
        A3 = self.det2x2(a1.n, -a2.n, a1.k, -a2.k)
        if A1 != 0 and A2 !=0 and A3 != 0:
            t1=self.det2x2(-(point1.x-point2.x), -a2.m, -(point1.y-point2.y), -a2.n)/A1
            s1=self.det2x2(a1.m,-(point1.x-point2.x),a1.n,-(point1.y-point2.y))/A1
            t2=self.det2x2(-(point1.x-point2.x), -a2.m, -(point1.z-point2.z), -a2.k)/A2
            s2=self.det2x2(a1.m, -(point1.x-point2.x), a1.k, -(point1.z-point2.z))/A2
            t3=self.det2x2(-(point1.y-point2.y), -a2.n, -(point1.z-point2.z), -a2.k)/A3
            s3=self.det2x2(a1.n, -(point1.y-point2.y), a1.k, -(point1.z-point2.z))/A3
            if t1==t2 and t2==t3 and s1 == s2 and s2 == s3:
                return Point(t1*a1.m+point1.x, t1*a1.n+point1.y, t1*a1.k+point1.z)
        return None

    def getDistanceBetweenTwoPoints(self, point1: Point, point2: Point):
        return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2+(point1.z-point2.z)**2)

    # 1 if point lies between 4 another, 0 - otherwise
    def checkIfPointBetween4Another(self, point0: Point, point1: Point, point2: Point, point3: Point, point4: Point):
        dist1 = self.getDistanceBetweenTwoPoints(point1, point2)
        dist2 = self.getDistanceBetweenTwoPoints(point0, point1)
        dist3 = self.getDistanceBetweenTwoPoints(point0, point2)

        dist4 = self.getDistanceBetweenTwoPoints(point3, point4)
        dist5 = self.getDistanceBetweenTwoPoints(point0, point3)
        dist6 = self.getDistanceBetweenTwoPoints(point0, point4)

        if (dist2<=dist1 and dist3<=dist1 and dist4>=dist5 and dist4>=dist6) :
            return 1
        return 0

    # a*x1+b*x2+c = 0
    def solveEquation(self, a, b, c):
        if a!=0:
            return Point(-c/a,0,0)
        elif b!=0:
            return Point(0, -c/b, 0)
        else :
            return Point(0,0,0)

    def findStraightOfPlanesIntersect(self, plane1: Plane, plane2: Plane):
        a = Vector(self.det2x2(plane1.B, plane1.C, plane2.B, plane2.C), -self.det2x2(plane1.A, plane1.C, plane2.A, plane2.C), self.det2x2(plane1.A, plane1.B, plane2.A, plane2.B))
        if plane1.A != 0:
            point = self.solveEquation(plane2.B-plane1.B/plane1.A*plane2.A, plane2.C-plane1.C/plane1.A*plane2.A, plane2.D-plane1.D/plane1.A*plane2.A)
            point1 = Point(-(plane1.B*point.x+plane1.C*point.y+plane1.D)/plane1.A,point.x, point.y)
            return Straight(point1, Point(a.m+point1.x, a.n+point1.y, a.k+point1.z))
        elif plane2.A != 0:
            point = self.solveEquation(plane1.B - plane2.B / plane2.A*plane1.A, plane1.C - plane2.C / plane2.A*plane1.A,
                                       plane1.D - plane2.D / plane2.A*plane1.A)
            point1 = Point(-(plane2.B * point.x + plane2.C * point.y + plane2.D) / plane2.A, point.x, point.y)
            return Straight(point1, Point(a.m + point1.x, a.n + point1.y, a.k + point1.z))
        else:
            detA = self.det2x2(plane1.B, plane1.C, plane2.B, plane2.C)
            y = self.det2x2(-plane1.D, plane1.C, -plane2.D, plane2.C)/detA
            z = self.det2x2(plane1.B, -plane1.D, plane2.B, -plane2.D)/detA
            point1 = Point(0, y, z)
            return Straight(point1, Point(a.m + point1.x, a.n + point1.y, a.k + point1.z))




