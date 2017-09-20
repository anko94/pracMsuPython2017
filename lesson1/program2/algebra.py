from lesson1.program2.point import Point
from lesson1.program2.plane import Plane

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