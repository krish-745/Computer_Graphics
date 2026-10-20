from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def drawLine(x0, y0, x1, y1):
	dx, dy = (x1-x0), (y1-y0)
	steps = max(abs(dx), abs(dy))          # greater of |dx|, |dy|
	x_inc, y_inc = dx / steps, dy / steps  # divide both by the greater one
	x, y = x0, y0
	glBegin(GL_POINTS)
	for _ in range(steps + 1):             # steps + 1 pixels
		glVertex2f(np.floor(x + 0.5), np.floor(y + 0.5))   # round, plot
		# Update x and y
		x, y = x + x_inc, y + y_inc
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(0.0, 0.0, 0.0)
	drawLine(100, 100, 250, 250)
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Simple DDA Line Drawing")
glutDisplayFunc(display)
glClearColor(1.0, 1.0, 1.0, 1.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, 500, 0, 500)
glutMainLoop()