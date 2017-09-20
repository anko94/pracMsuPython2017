from lesson1.program2.point import Point
from lesson1.program2.straight import Straight
from lesson1.program2.triangle import Triangle
from lesson1.program2.plane import Plane
from lesson1.program2.algebra import Algebra
import numpy as np

if __name__ == "__main__":
    alg = Algebra()
    triangle1 = Triangle(Point(1,-2,0), Point(2,0,-1), Point(0,-1,2))
    triangle2 = Triangle(Point(3,1,2), Point(5,6,7), Point(9,11,-2))
    plane1 = alg.getPlane(triangle1.point1, triangle1.point2, triangle1.point3)
    plane2 = alg.getPlane(triangle2.point1, triangle2.point2, triangle2.point3)

    planeRelationship = alg.planeRelationship()

    if planeRelationship == 1:
        print("Triangles don't intersect")
    elif planeRelationship == 0:
        straight1 = Straight(triangle1.point1, triangle1.point2)
        straight2 = Straight(triangle1.point1, triangle1.point3)
        straight3 = Straight(triangle1.point2, triangle1.point3)



    # print(np.linalg.matrix_rank(np.matrix([[1,1],[1,2]])))
    # plane = alg.getPlane(Point(3,1,2), Point(5,6,7), Point(9,11,-2))
    # plane1 = Plane(1,1,1,1)
    # plane2 = Plane(1, 2, 1, 1)
    # print(alg.planeRelationship(plane1, plane2))