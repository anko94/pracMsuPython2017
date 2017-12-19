import pywavefront
from OpenGL.GL import *
from OpenGL.GLUT import *


# Процедура подготовки шейдера (тип шейдера, текст шейдера)
def create_shader(shader_type, source):
    # Создаем пустой объект шейдера
    shader = glCreateShader(shader_type)
    # Привязываем текст шейдера к пустому объекту шейдера
    glShaderSource(shader, source)
    # Компилируем шейдер
    glCompileShader(shader)
    # Возвращаем созданный шейдер
    return shader

# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    # Обработчики специальных клавиш
    if key == GLUT_KEY_UP:  # Клавиша вверх
        glRotatef(5, 1, 0, 0)  # Вращаем на 5 градусов по оси X
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        glRotatef(-5, 1, 0, 0)  # Вращаем на -5 градусов по оси X
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        glRotatef(5, 0, 1, 0)  # Вращаем на 5 градусов по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        glRotatef(-5, 0, 1, 0)  # Вращаем на -5 градусов по оси Y


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    glColorPointer(3, GL_FLOAT, 0, pointcolor)

    glDrawArrays(GL_TRIANGLES, 0, len(pointdata))

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)

    glutSwapBuffers()


if __name__ == '__main__':
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInit(sys.argv)
    windowWidth = glutGet(GLUT_WINDOW_WIDTH)
    windowHeight = glutGet(GLUT_WINDOW_HEIGHT)
    glutCreateWindow(b"Program!")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutSpecialFunc(specialkeys)
    glClearColor(0.2, 0.2, 0.2, 1)
    program = glCreateProgram()
    # Положение вершин не меняется
    # Цвет вершины - такой же как и в массиве цветов
    vertex = create_shader(GL_VERTEX_SHADER, """
        varying vec4 vertex_color;
                    void main(){
                        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                        vertex_color = gl_Color;
                    }""")

    # Определяет цвет каждого фрагмента как "смешанный" цвет его вершин
    fragment = create_shader(GL_FRAGMENT_SHADER, """
        varying vec4 vertex_color;
                    void main() {
                        gl_FragColor = vertex_color;
        }""")

    glAttachShader(program, vertex)
    glAttachShader(program, fragment)
    glLinkProgram(program)
    glUseProgram(program)

    name = 'model2bis.obj'
    meshes = pywavefront.Wavefront(name)
    ps = pywavefront.ObjParser(meshes, name)
    ps.read_file(name)
    points=ps.material.vertices
    pointcolor = []
    pointdata = []
    for i in range(int(len(points)/3)):
        pointcolor.append([1,0,0])
        pointdata.append([points[i*3], points[i*3+1], points[i*3+2]])

    for i in range(len(pointdata)):
        pointdata[i][0] /= 10
        pointdata[i][1] /= 10
        pointdata[i][2] /= 10

    glutMainLoop()