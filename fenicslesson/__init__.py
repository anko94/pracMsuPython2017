from dolfin import *
from dolfin.cpp.common import has_petsc
from dolfin.cpp.io import File
from dolfin.cpp.la import PETScOptions
import numpy as np
from matplotlib import tri, pyplot as plt


if __name__ == "__main__":
    mesh_size = 10
    p1 = Point(0, 0)
    p2 = Point(DOLFIN_PI, DOLFIN_PI)
    mesh = RectangleMesh(p1,p2,mesh_size,mesh_size)
    V = FunctionSpace(mesh, "P", 1)

    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Constant(0)
    g = Expression("(pi-x[1])/pi*sin(4*x[0]) + x[1]/pi*sin(6*x[0])", degree=3)
    a = dot(grad(u), grad(v)) * dx
    L = f * v * dx - g * v * ds

    # Define boundary condition values
    u0 = Expression("x[0]/pi*cos(4*x[1])", degree=3)

    # Define boundary conditions
    def boundary1(x, on_boundary):
        return on_boundary and (x[0] < DOLFIN_EPS or x[0] > DOLFIN_PI - DOLFIN_EPS)
    bc0 = DirichletBC(V, u0, boundary1)

    # Set PETSc MUMPS paramter (this is required to prevent a memory error
    # in some cases when using MUMPS LU solver).
    if has_petsc():
        PETScOptions.set("mat_mumps_icntl_14", 40.0)

    # Compute solution
    u = Function(V)
    solve(a == L, u, bc0)

    # Write solution to file
    File("u.pvd") << u

    u_A = Expression("(1/4*sinh(4*x[1])-1/4*cosh(4*pi)/sinh(4*pi)*cosh(4*x[1]))*sin(4*x[0]) + 1/(6*sinh(6*pi))*cosh(6*x[1])*sin(6*x[0]) + sinh(4*x[0])/sinh(4*pi)*cos(4*x[1])", degree=3)
    error_L2 = errornorm(u_A, u, 'L2')
    print(error_L2)

    vertex_values_u_A = u_A.compute_vertex_values(mesh)
    vertex_values_u = u.compute_vertex_values(mesh)
    error_C = np.max(np.abs(vertex_values_u-vertex_values_u_A))
    print(error_C)

    n=mesh.num_vertices()
    d=mesh.geometry().dim()
    mesh_coordinates=mesh.coordinates().reshape((n, d))
    triangles = np.asarray([cell.entities(0) for cell in cells(mesh)])
    triangulation = tri.Triangulation(mesh_coordinates[:, 0], mesh_coordinates[:, 1], triangles)

    fig = plt.figure()
    zfaces = np.asarray([u(cell.midpoint()) for cell in cells(mesh)])
    plt.tripcolor(triangulation, facecolors=zfaces, edgecolors='k')
    plt.savefig('u_midpoint.png')

    zfaces = np.asarray([u_A(cell.midpoint()) for cell in cells(mesh)])
    plt.tripcolor(triangulation, facecolors=zfaces, edgecolors='k')
    plt.savefig('u_A_midpoint.png')
