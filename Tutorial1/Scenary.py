from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500


# ----------------------------
# Draw Rectangle
# ----------------------------
def rectangle(x1, y1, x2, y2):

    glBegin(GL_QUADS)

    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)

    glEnd()



# ----------------------------
# Draw Triangle
# ----------------------------
def triangle(x1,y1,x2,y2,x3,y3):

    glBegin(GL_TRIANGLES)

    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)

    glEnd()



# ----------------------------
# Natural Scene
# ----------------------------
def scene():


    # -------- Sky --------
    glColor3f(0.5,0.8,1.0)
    rectangle(0,200,500,500)



    # -------- Ground --------
    glColor3f(0.0,0.7,0.0)
    rectangle(0,0,500,200)



    # -------- Sun --------
    glColor3f(1.0,1.0,0.0)

    triangle(
        400,420,
        360,350,
        440,350
    )


    # -------- House Body --------
    glColor3f(0.8,0.4,0.2)

    rectangle(
        150,100,
        300,250
    )


    # -------- House Roof --------
    glColor3f(0.8,0.0,0.0)

    triangle(
        120,250,
        330,250,
        225,350
    )


    # -------- Door --------
    glColor3f(0.4,0.2,0.0)

    rectangle(
        210,100,
        250,180
    )


    # -------- Tree Trunk --------
    glColor3f(0.5,0.25,0.0)

    rectangle(
        50,100,
        90,250
    )


    # -------- Tree Leaves --------
    glColor3f(0.0,0.5,0.0)

    triangle(
        20,250,
        120,250,
        70,380
    )


    triangle(
        30,320,
        110,320,
        70,430
    )



    # -------- Clouds --------

    glColor3f(1.0,1.0,1.0)

    rectangle(80,400,160,430)

    rectangle(120,420,200,450)

    rectangle(300,400,380,430)




# ----------------------------
# Coordinate Setup
# ----------------------------
def iterate():

    glViewport(0,0,w,h)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glOrtho(0,500,0,500,0,1)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()



# ----------------------------
# Display
# ----------------------------
def showScreen():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    iterate()

    scene()

    glutSwapBuffers()



# ----------------------------
# Main Program
# ----------------------------

glutInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

glutInitWindowSize(w,h)

glutInitWindowPosition(0,0)

glutCreateWindow(
    b"PyOpenGL Natural Scene"
)


glutDisplayFunc(showScreen)

glutIdleFunc(showScreen)

glutMainLoop()