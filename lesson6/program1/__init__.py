from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random

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
    # Сообщаем о необходимости использовать глобального массива pointcolor
    global pointcolor
    # Обработчики специальных клавиш
    if key == GLUT_KEY_UP:          # Клавиша вверх
        glRotatef(5, 1, 0, 0)       # Вращаем на 5 градусов по оси X
    if key == GLUT_KEY_DOWN:        # Клавиша вниз
        glRotatef(-5, 1, 0, 0)      # Вращаем на -5 градусов по оси X
    if key == GLUT_KEY_LEFT:        # Клавиша влево
        glRotatef(5, 0, 1, 0)       # Вращаем на 5 градусов по оси Y
    if key == GLUT_KEY_RIGHT:       # Клавиша вправо
        glRotatef(-5, 0, 1, 0)      # Вращаем на -5 градусов по оси Y
    if key == GLUT_KEY_END:         # Клавиша END
        # Заполняем массив pointcolor случайными числами в диапазоне 0-1
        pointcolor = [[random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],

                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],

                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],

                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],

                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],

                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()]
                      ]

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(4, GL_FLOAT, 0, pointdata)
    glColorPointer(4, GL_FLOAT, 0, pointcolor)
    glDrawArrays(GL_QUADS, 0, 24)
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)
    glutSwapBuffers()

if __name__ == '__main__':
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(50, 50)
    glutInit(sys.argv)
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

