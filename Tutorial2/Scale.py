from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

w,h= 500,500

def square(pc):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(pc[0][0], pc[0][1]) # Coordinates for the bottom left point
    glVertex2f(pc[1][0], pc[1][1]) # Coordinates for the bottom right point
    glVertex2f(pc[2][0], pc[2][1]) # Coordinates for the top right point
    glVertex2f(pc[3][0], pc[3][1]) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

def get_scale2d(factor):
    R = np.array([[factor, 0, 0], [0, factor, 0], [0, 0, 1]],dtype=np.float32)
    return np.transpose(R)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    pc = np.array([[100, 100, 1], [200, 100, 1], [200, 200, 1], [100, 200, 1]],dtype=np.float32)
    pc_new = np.array([i @ get_scale2d(1.5) for i in pc],dtype=np.float32)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0)  # Set the color to pink
    square(pc)
    square(pc_new) # Draw a square using our function
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(w, h)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow(b"OpenGL Coding Practice - Simple Square") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop
