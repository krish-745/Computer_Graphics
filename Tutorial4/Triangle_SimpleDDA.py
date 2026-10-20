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
	for _ in range(steps + 1):
		glVertex2f(np.floor(x + 0.5), np.floor(y + 0.5))   # round, plot
		# Update x and y
		x, y = x + x_inc, y + y_inc
	glEnd()

def drawTriangle(p, q, r):
	drawLine(p[0], p[1], q[0], q[1])       # P -> Q
	drawLine(q[0], q[1], r[0], r[1])       # Q -> R
	drawLine(r[0], r[1], p[0], p[1])       # R -> P

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(0.0, 0.0, 0.0)
	drawTriangle((100, 100), (300, 100), (200, 300))
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Triangle using Simple DDA")
glutDisplayFunc(display)
glClearColor(1.0, 1.0, 1.0, 1.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, 500, 0, 500)
glutMainLoop()