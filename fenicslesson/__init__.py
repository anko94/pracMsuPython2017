from fenics import *
import numpy as np
from matplotlib import tri, pyplot as plt

if __name__ == "__main__":
    mesh_size = 40
    p1 = Point(0, 0)
    p2 = Point(FENICS_PI, FENICS_PI)
    mesh = RectangleMesh(p1,p2,mesh_size,mesh_size)
    V = FunctionSpace(mesh, "P", 5)

    # boundary_parts = FacetFunction('size_t', mesh)
    # up = AutoSubDomain(lambda x: near(x[1], FENICS_PI, FENICS_EPS))
    # bottom = AutoSubDomain(lambda x: near(x[1], 0, FENICS_EPS))
    # up.mark(boundary_parts, 2)
    # bottom.mark(boundary_parts, 2)
    # dsn = Measure("ds", subdomain_id=2, subdomain_data=boundary_parts)

    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Constant(0)
    g = Expression("(pi-x[1])/pi*sin(4*x[0]) - x[1]/pi*sin(6*x[0])", degree=5)
    a = dot(grad(u), grad(v)) * dx
    L = f * v * dx - g * v * ds

    # Define boundary condition values
    u0 = Expression("x[0]/pi*cos(4*x[1])", degree=5)

    # Define boundary conditions
    def boundary1(x, on_boundary):
        return on_boundary and (near(x[0], 0, FENICS_EPS) or near(x[0], FENICS_PI, FENICS_EPS))
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
    u_A = Expression(
        "sinh(4*x[0])/sinh(4*pi)*cos(4*x[1])+(sinh(4*x[1])/4-cosh(4*pi)/(4*sinh(4*pi))*cosh(4*x[1]))*sin(4*x[0])+1/(6*sinh(6*pi))*cosh(6*x[1])*sin(6*x[0])",
        degree=5)
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