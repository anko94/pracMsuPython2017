from OpenGL.GL import *
from OpenGL.GLUT import *
import math
import numpy as np


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


def mouseMotion(x, y):
    global lastTime
    global horizontalAngle
    global verticalAngle
    currentTime = glutGet(GLUT_ELAPSED_TIME)
    deltaTime = currentTime - lastTime
    lastTime = currentTime

    #Compute new orientation
    horizontalAngle += mouseSpeed * deltaTime * (windowHeight / 2 - x)
    verticalAngle += mouseSpeed * deltaTime * (windowWidth / 2 - y)

    direction = [math.cos(verticalAngle) * math.sin(horizontalAngle), math.sin(verticalAngle), math.cos(verticalAngle) * math.cos(horizontalAngle)]
    right = [math.sin(horizontalAngle - 3.14/2.0), 0, math.cos(horizontalAngle - 3.14/2.0)]
    up = np.cross(np.array(direction), np.array(right)).toList()


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    # Обработчики специальных клавиш
    if key == GLUT_KEY_UP:          # Клавиша вверх
        for i in range(len(position)):
            position[i] += direction[i] * deltaTime * speed
    if key == GLUT_KEY_DOWN:        # Клавиша вниз
        for i in range(len(position)):
            position[i] -= direction[i] * deltaTime * speed
    if key == GLUT_KEY_LEFT:        # Клавиша влево
        for i in range(len(position)):
            position[i] -= right[i] * deltaTime * speed
    if key == GLUT_KEY_RIGHT:       # Клавиша вправо
        for i in range(len(position)):
            position[i] += right[i] * deltaTime * speed


def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    glColorPointer(3, GL_FLOAT, 0, pointcolor)
    glDrawArrays(GL_QUADS, 0, 24)
    glutSolidCone(1, 3, 50, 50)

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)
    glutSwapBuffers()


if __name__ == '__main__':
    # variables
    position = [0, 0, 5]
    right = []
    horizontalAngle = 3.14
    verticalAngle = 0.0
    initialFoV = 45.0
    speed = 3.0
    mouseSpeed = 0.005
    lastTime = 0
    direction = []
    deltaTime = 0

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glEnable(GL_DEPTH_TEST);
    glutInit(sys.argv)
    windowWidth = glutGet(GLUT_WINDOW_WIDTH)
    windowHeight = glutGet(GLUT_WINDOW_HEIGHT)
    glutCreateWindow(b"Program!")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutSpecialFunc(specialkeys)
    glutPassiveMotionFunc(mouseMotion)
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
    pointdata = [[0.5, -0.5, 0.5], [0.5,  0.5, 0.5], [-0.5,  0.5, 0.5], [-0.5, -0.5, 0.5],
                 [0.5, -0.5, -0.5], [0.5,  0.5, -0.5], [0.5,  0.5,  0.5], [0.5, -0.5,  0.5],
                 [-0.5, -0.5,  0.5], [-0.5,  0.5,  0.5], [-0.5,  0.5, -0.5], [-0.5, -0.5, -0.5],
                 [0.5,  0.5,  0.5], [0.5,  0.5, -0.5 ], [-0.5,  0.5, -0.5], [-0.5,  0.5,  0.5],
                 [0.5, -0.5, -0.5], [0.5, -0.5,  0.5], [-0.5, -0.5,  0.5], [-0.5, -0.5, -0.5],
                 [-0.5, -0.5, -0.5], [-0.5,  0.5, -0.5], [0.5,  0.5, -0.5], [0.5, -0.5, -0.5]]
    pointcolor = [[1.0,  1.0, 1.0],
                  [1.0,  0.0,  1.0],
                  [1.0,  0.0,  1.0],
                  [1.0,  0.0,  1.0],

                  [1.0,  0.0,  1.0],
                  [1.0,  0.0,  1.0],
                  [1.0, 1.0, 1.0],
                  [1.0, 0.0, 1.0],

                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],

                  [1.0, 1.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],

                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 1.0, 1.0],
                  [1.0, 0.0, 1.0],

                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0]
                  ]
    glutMainLoop()

