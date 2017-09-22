from lesson1.program2.algebra import Algebra
from lesson1.program2.data.plane import Plane
from lesson1.program2.data.point import Point
from lesson1.program2.data.straight import Straight
from lesson1.program2.data.triangle import Triangle
import math

# 1 if one triangle lies in another, 0 - otherwise
def checkIfOneTriangleLiesInAnother(triangle1: Triangle, triangle2: Triangle, plane1: Plane, plane2: Plane):
    lies = 0
    sum = 0
    plane11 = alg.getPlane(triangle1.point1, triangle1.point2, Point(plane1.A+triangle1.point2.x, plane1.B+triangle1.point2.y, plane1.C+triangle1.point2.z))
    plane12 = alg.getPlane(triangle1.point2, triangle1.point3, Point(plane1.A+triangle1.point3.x, plane1.B+triangle1.point3.y, plane1.C+triangle1.point3.z))
    plane13 = alg.getPlane(triangle1.point3, triangle1.point1, Point(plane1.A+triangle1.point1.x, plane1.B+triangle1.point1.y, plane1.C+triangle1.point1.z))
    plane21 = alg.getPlane(triangle2.point1, triangle2.point2, Point(plane2.A+triangle2.point2.x, plane2.B+triangle2.point2.y, plane2.C+triangle2.point2.z))
    plane22 = alg.getPlane(triangle2.point2, triangle2.point3, Point(plane2.A+triangle2.point3.x, plane2.B+triangle2.point3.y, plane2.C+triangle2.point3.z))
    plane23 = alg.getPlane(triangle2.point3, triangle2.point1, Point(plane2.A+triangle2.point1.x, plane2.B+triangle2.point1.y, plane2.C+triangle2.point1.z))
    planes1 = [plane11, plane12, plane13]
    points1 = [triangle1.point3, triangle1.point1, triangle1.point2]
    planes2 = [plane21, plane22, plane23]
    points2 = [triangle2.point3, triangle2.point1, triangle2.point2]
    for i in range(len(planes1)):
        if not(planes1[i].tryPoint(points1[i]) >= 0 and planes1[i].tryPoint(points2[0]) >= 0 and planes1[i].tryPoint(points2[1]) >= 0 and planes1[i].tryPoint(points2[2]) >= 0 or \
                planes1[i].tryPoint(points1[i]) < 0 and planes1[i].tryPoint(points2[0]) < 0 and planes1[i].tryPoint(points2[1]) < 0 and planes1[i].tryPoint(points2[2]) < 0):
            break
        sum += 1
    if sum == 3:
        lies = 1
    sum = 0
    if lies == 0:
        for i in range(len(planes2)):
            if not(planes2[i].tryPoint(points2[i]) >= 0 and planes2[i].tryPoint(points1[0]) >= 0 and planes2[i].tryPoint(points1[1]) >= 0 and planes2[i].tryPoint(points1[2]) >= 0 or \
                   planes2[i].tryPoint(points2[i]) < 0 and planes2[i].tryPoint(points1[0]) < 0 and planes2[i].tryPoint(points1[1]) < 0 and planes2[i].tryPoint(points1[2]) < 0):
                break
            sum += 1
        if sum == 3:
            lies = 1
    return lies

if __name__ == "__main__":
    alg = Algebra()
    # 1 if triangles intersect, 0 - otherwise
    isTrianglesIntersect = 0
    triangle1 = Triangle(Point(1, -2, 0), Point(2, 0, -1), Point(0, -1, 2))
    triangle2 = Triangle(Point(3, 1, 2), Point(5, 6, 7), Point(9, 11, -2))
    plane1 = alg.getPlane(triangle1.point1, triangle1.point2, triangle1.point3)
    plane2 = alg.getPlane(triangle2.point1, triangle2.point2, triangle2.point3)

    planeRelationship = alg.planeRelationship(plane1, plane2)

    if planeRelationship == 0:
        straight11 = Straight(triangle1.point1, triangle1.point2)
        straight12 = Straight(triangle1.point1, triangle1.point3)
        straight13 = Straight(triangle1.point2, triangle1.point3)
        straight21 = Straight(triangle2.point1, triangle2.point2)
        straight22 = Straight(triangle2.point1, triangle2.point3)
        straight23 = Straight(triangle2.point2, triangle2.point3)
        straights1 = [straight11, straight12, straight13]
        straights2 = [straight21, straight22, straight23]
        for i in range(len(straights1)):
            for j in range(len(straights2)):
                vect1 = straights1[i].a
                vect2 = straights2[j].a
                cos = (vect1.m * vect2.m + vect1.n * vect2.n + vect1.k * vect2.k) / (
                math.sqrt(vect1.m * vect1.m + vect1.n * vect1.n + vect1.k * vect1.k)
                * math.sqrt(vect2.m * vect2.m + vect2.n * vect2.n + vect2.k * vect2.k))
                if cos == -1 or cos == 1:
                    point1 = straights1[i].point
                    if straights2[j].isPointOnTheStraight(point1) == 1:
                        isTrianglesIntersect = 1
                        break
                else :
                    point2 = alg.solveSystemOfEquations(straights1[i], straights2[j])
                    if alg.checkIfPointBetween4Another(point2, straights1[i].point0, straights1[i].point2, straights2[j].point0, straights2[j].point2) == 1:
                        isTrianglesIntersect = 1
                        break
            if isTrianglesIntersect == 1:
                break
        if isTrianglesIntersect == 0:
            isTrianglesIntersect = checkIfOneTriangleLiesInAnother(triangle1, triangle2, plane1, plane2)
    elif planeRelationship == 2:
        straightIntersect = alg.findStraightOfPlanesIntersect(plane1, plane2)
        #ToDo

    if isTrianglesIntersect == 1:
        print("Triangles intersect")
    else :
        print("Triangles don't intersect")
                # print(np.linalg.matrix_rank(np.matrix([[1,1],[1,2]])))
                # plane = alg.getPlane(Point(3,1,2), Point(5,6,7), Point(9,11,-2))
                # plane1 = Plane(1,1,1,1)
                # plane2 = Plane(1, 2, 1, 1)
                # print(alg.planeRelationship(plane1, plane2))
