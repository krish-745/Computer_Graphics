from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawLine(x0, y0, x1, y1):
    dx, dy = (x1 - x0), (y1 - y0)
    d = 2 * dy - dx
    dE, dNE = 2 * dy, 2 * (dy - dx)
    x, y = x0, y0

    glBegin(GL_POINTS)
    glVertex2f(x, y)

    while x != x1:
        if d <= 0:
            d += dE
        else:
            d += dNE
            y += 1

        x += 1
        glVertex2f(x, y)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    drawLine(100, 100, 250, 250)

    glFinish()
    glReadBuffer(GL_BACK)
    glPixelStorei(GL_PACK_ALIGNMENT, 1)

    pixels = glReadPixels(
        0, 0, 500, 500, GL_RGB, GL_UNSIGNED_BYTE
    )

    image = Image.frombytes("RGB", (500, 500), pixels)
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    glutSwapBuffers()
    
    # Opens the image natively in Windows
    image.show() 

# Initialization
glutInit([])
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
# Use a hidden window or allow it to flash briefly
window = glutCreateWindow(b"Bresenham Line Drawing")

glutDisplayFunc(display)
glClearColor(1.0, 1.0, 1.0, 1.0)
glViewport(0, 0, 500, 500)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, 500, 0, 500)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Render once
display()

glutDestroyWindow(window)