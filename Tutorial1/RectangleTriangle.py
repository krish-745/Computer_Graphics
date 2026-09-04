from OpenGL.GL import *      # OpenGL drawing functions
from OpenGL.GLUT import *    # Window and event handling
from OpenGL.GLU import *     # Utility functions


w, h = 500, 500


# ------------------------------------------------
# Draw Square
# ------------------------------------------------
def square():

    glBegin(GL_QUADS)

    # Square coordinates
    glVertex2f(300, 300)   # Bottom-left
    glVertex2f(400, 300)   # Bottom-right
    glVertex2f(400, 400)   # Top-right
    glVertex2f(300, 400)   # Top-left

    glEnd()



# ------------------------------------------------
# Draw Rectangle
# ------------------------------------------------
def rectangle():

    glBegin(GL_QUADS)

    # Rectangle coordinates
    glVertex2f(50, 100)    # Bottom-left
    glVertex2f(250, 100)   # Bottom-right
    glVertex2f(250, 200)   # Top-right
    glVertex2f(50, 200)    # Top-left

    glEnd()



# ------------------------------------------------
# Draw Triangle
# ------------------------------------------------
def triangle():

    glBegin(GL_TRIANGLES)

    # Triangle coordinates
    glVertex2f(100, 350)   # Top vertex
    glVertex2f(50, 250)    # Bottom-left
    glVertex2f(150, 250)   # Bottom-right

    glEnd()



# ------------------------------------------------
# Coordinate Setup
# ------------------------------------------------
def iterate():

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # 2D coordinate system
    glOrtho(0, 500, 0, 500, 0, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



# ------------------------------------------------
# Display Function
# ------------------------------------------------
def showScreen():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    iterate()


    # Draw Rectangle (Green)
    glColor3f(0.0, 1.0, 0.0)
    rectangle()


    # Draw Square (Red)
    glColor3f(1.0, 0.0, 0.0)
    square()


    # Draw Triangle (Blue)
    glColor3f(0.0, 0.0, 1.0)
    triangle()


    glutSwapBuffers()



# ------------------------------------------------
# Main Program
# ------------------------------------------------

glutInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

glutInitWindowSize(w, h)

glutInitWindowPosition(0, 0)


glutCreateWindow(
    b"Square Rectangle Triangle - PyOpenGL"
)


glutDisplayFunc(showScreen)

glutIdleFunc(showScreen)


glutMainLoop()