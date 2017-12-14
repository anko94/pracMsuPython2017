from OpenGL.GL import *
from OpenGL.GLUT import *
import math


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

    for i in range(6):
        glBegin(GL_POLYGON)
        glColor3f(pointcolor[i][0], pointcolor[i][1], pointcolor[i][2])
        glVertex3f(pointdata[i*4][0], pointdata[i*4][1], pointdata[i*4][2])
        glVertex3f(pointdata[i*4+1][0], pointdata[i*4+1][1], pointdata[i*4+1][2])
        glVertex3f(pointdata[i*4+2][0], pointdata[i*4+2][1], pointdata[i*4+2][2])
        glVertex3f(pointdata[i*4+3][0], pointdata[i*4+3][1], pointdata[i*4+3][2])
        glEnd()

    # cone's pinnacle
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 0)
    glVertex3f(conepointdata[0][0], conepointdata[0][1], conepointdata[0][2])
    for angle in range(361):
        x = math.sin(math.radians(angle))
        y = math.cos(math.radians(angle))
        glColor3f(1,1,0)
        glVertex2f(x, y)
    glEnd()

    # bottom of cone
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0, 0)
    glVertex3f(conepointdata[1][0], conepointdata[1][1], conepointdata[1][2])
    for angle in range(361):
        x = math.sin(math.radians(angle))
        y = math.cos(math.radians(angle))
        glColor3f(1, 0, 0)
        glVertex2f(x, y)
    glEnd()

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

    pointdata = []
    conepointdata = []
    with open("scene.obj") as obj:
        data = obj.read()
    lines = data.splitlines()
    cube = 0
    cone = 0
    for line in lines:
        elem = line.split(" ")
        if len(elem)>1 and elem[1].__eq__("cube"):
            cube = 1
            cone = 0
        if len(elem)>1 and elem[1].__eq__("cone"):
            cube = 0
            cone = 1
        if cube == 1 and elem[0].__eq__("v"):
            pointdata.append([float(elem[1]), float(elem[2]), float(elem[3])])
        if cone == 1 and elem[0].__eq__("v"):
            conepointdata.append([float(elem[1]), float(elem[2]), float(elem[3])])

    pointcolor = [
                  [0, 1.0, 0],
                  [1.0, 0, 0],
                  [1.0, 1.0, 0.0],
                  [1.0, 1.0, 0.0],
                  [1.0, 1.0, 0.0],
                  [1.0, 1.0, 0.0]
                  ]
    glutMainLoop()
