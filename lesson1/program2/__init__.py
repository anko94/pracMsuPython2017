from lesson1.program2.algebra import Algebra
from lesson1.program2.data.plane import Plane
from lesson1.program2.data.point import Point
from lesson1.program2.data.straight import Straight
from lesson1.program2.data.triangle import Triangle
import math

# 1 if one triangle lies in another, 0 - otherwise
from lesson1.program2.data.vector import Vector


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
    accuracy = 0.000000000001
    triangle1 = Triangle(Point(2, -5, -1), Point(-22/13, -19/13, 0), Point(-3, 1/2, 0))
    triangle2 = Triangle(Point(-1, 1, 1), Point(-24/13, -42/13, 1), Point(1, 6, 6))
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
                if abs(cos + 1)<accuracy or abs(cos - 1)<accuracy:
                    point1 = straights1[i].point0
                    if abs(straights2[j].isPointOnTheStraight(point1) - 1)<accuracy:
                        isTrianglesIntersect = 1
                        break
                else :
                    point2 = alg.solveSystemOfEquations(straights1[i], straights2[j])
                    if abs(alg.checkIfPointBetween4Another(point2, straights1[i].point0, straights1[i].point2, straights2[j].point0, straights2[j].point2) - 1)<accuracy:
                        isTrianglesIntersect = 1
                        break
            if isTrianglesIntersect == 1:
                break
        if isTrianglesIntersect == 0:
            isTrianglesIntersect = checkIfOneTriangleLiesInAnother(triangle1, triangle2, plane1, plane2)
    elif planeRelationship == 2:
        straightIntersect = alg.findStraightOfPlanesIntersect(plane1, plane2)
        straight11 = Straight(triangle1.point1, triangle1.point2)
        straight12 = Straight(triangle1.point1, triangle1.point3)
        straight13 = Straight(triangle1.point2, triangle1.point3)
        straight21 = Straight(triangle2.point1, triangle2.point2)
        straight22 = Straight(triangle2.point1, triangle2.point3)
        straight23 = Straight(triangle2.point2, triangle2.point3)
        straights1 = [straight11, straight12, straight13]
        straights2 = [straight21, straight22, straight23]
        c1 = 0
        c2 = 0
        for i in range(len(straights1)):
            if alg.solveSystemOfEquations(straights1[i], straightIntersect) != None:
                c1=1
                break
        for i in range(len(straights2)):
            if alg.solveSystemOfEquations(straights2[i], straightIntersect) != None:
                c2 = 1
                break
        if c1==1 and c2==1:
            points = []
            point11 = alg.solveSystemOfEquations(straights1[0], straightIntersect)
            if point11!=None:
                point11.mark = 1
                points.append(point11)
            point12 = alg.solveSystemOfEquations(straights1[1], straightIntersect)
            if point12!=None:
                point12.mark = 1
                points.append(point12)
            point13 = alg.solveSystemOfEquations(straights1[2], straightIntersect)
            if point13!=None:
                point13.mark = 1
                points.append(point13)
            point21 = alg.solveSystemOfEquations(straights2[0], straightIntersect)
            if point21!=None:
                point21.mark = 2
                points.append(point21)
            point22 = alg.solveSystemOfEquations(straights2[1], straightIntersect)
            if point22!=None:
                point22.mark = 2
                points.append(point22)
            point23 = alg.solveSystemOfEquations(straights2[2], straightIntersect)
            if point23!=None:
                point23.mark = 2
                points.append(point23)
            point3 = points[0]
            point4 = points[1]
            vMain = Vector(point4.x-point3.x,point4.y-point3.y, point4.z-point3.z)
            pointsD = []
            for i in range(len(points)):
                point4 = points[i]
                v = Vector(point4.x-point3.x,point4.y-point3.y, point4.z-point3.z)
                p = alg.getDistanceBetweenTwoPoints(point3, point4)
                if v.m*vMain.m+v.n*vMain.n+v.k*vMain.k >= 0:
                    pointsD.append(p)
                else:
                    pointsD.append(-p)
            minValue = 0
            minIndex = 0
            for i in range(len(pointsD)):
                minValue = pointsD[i]
                minIndex = i
                for j in range(i, len(pointsD)):
                    if minValue > pointsD[j]:
                        minValue = pointsD[j]
                        minIndex = j
                pointsD[minIndex] =  pointsD[i]
                pointsD[i] = minValue
                a = points[minIndex]
                points[minIndex] = points[i]
                points[i] = a
            for i in range(len(points)-1):
                point3 = points[i]
                point4 = points[i+1]
                if abs(point3.x-point4.x)<accuracy and abs(point3.y-point4.y)<accuracy and abs(point3.z-point4.z)<accuracy and point3.mark != point4.mark:
                    isTrianglesIntersect = 1
                    break
            if isTrianglesIntersect == 0:
                markq = points[0].mark
                c = 0
                for i in range(len(points)):
                    if points[i].mark != markq:
                        c = c+1
                        markq = points[i].mark
                if c!=1:
                    isTrianglesIntersect = 1

    if isTrianglesIntersect == 1:
        print("Triangles intersect")
    else :
        print("Triangles don't intersect")
