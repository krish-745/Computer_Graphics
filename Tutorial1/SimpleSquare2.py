from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Window size
w, h = 500, 500


# -----------------------------
# Draw Square
# -----------------------------
def square():

    glBegin(GL_QUADS)

    # Vertex order:
    # Bottom-left
    # Bottom-right
    # Top-right
    # Top-left

    glVertex2f(100, 100)
    glVertex2f(300, 100)
    glVertex2f(300, 300)
    glVertex2f(100, 300)

    glEnd()


# -----------------------------
# Set Coordinate System
# -----------------------------
def iterate():

    glViewport(0, 0, w, h)

    # Projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # 2D coordinate system
    glOrtho(0, 500, 0, 500, 0, 1)


    # ModelView matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



# -----------------------------
# Display Function
# -----------------------------
def showScreen():

    # Clear previous frame
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    # Setup coordinate system
    iterate()


    # Set square color
    # RGB values range 0.0 - 1.0
    glColor3f(1.0, 0.0, 0.0)


    # Draw square
    square()


    # Display rendered image
    glutSwapBuffers()



# -----------------------------
# Main Program
# -----------------------------

glutInit()

# Color mode
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Window size
glutInitWindowSize(w, h)

# Window position
glutInitWindowPosition(0,0)


# Create window
glutCreateWindow(
    b"PyOpenGL Simple Square"
)


# Register display callback
glutDisplayFunc(showScreen)

# Continuously refresh
glutIdleFunc(showScreen)


# Start OpenGL loop
glutMainLoop()