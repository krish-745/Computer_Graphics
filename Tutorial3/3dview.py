import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


screen_width = 800
screen_height = 800


class Pyramid:

    # Vertices are directly defined in an angled 3D position
    # No glRotatef(), glTranslatef(), or glScalef() is used
    vertices = (
        ( 1.13, -2.56, -12.04),   # 0
        ( 3.01, -1.20, -8.78),    # 1
        (-0.45, -1.20, -6.78),    # 2
        (-2.33, -2.56, -10.04),   # 3
        (-0.34,  1.88, -10.59)    # 4 - top
    )

    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),

        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4)
    )

    triangles = (
        (0, 1, 4),
        (1, 2, 4),
        (2, 3, 4),
        (3, 0, 4)
    )

    base = (0, 1, 2, 3)

    def draw(self):

        # Draw triangular sides
        glBegin(GL_TRIANGLES)

        for triangle in self.triangles:

            glColor3f(1.0, 0.5, 0.0)

            for vertex in triangle:
                glVertex3fv(self.vertices[vertex])

        glEnd()


        # Draw bottom/base
        glBegin(GL_QUADS)

        glColor3f(1.0, 0.5, 0.0)

        for vertex in self.base:
            glVertex3fv(self.vertices[vertex])

        glEnd()


        # Draw blue edges
        glLineWidth(4)

        glBegin(GL_LINES)

        glColor3f(0.0, 0.0, 1.0)

        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])

        glEnd()


def main():

    pygame.init()

    display = (screen_width, screen_height)

    pygame.display.set_mode(
        display,
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption("Static 3D Pyramid")

    # Projection only
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(
        45,
        screen_width / screen_height,
        0.1,
        50.0
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_DEPTH_TEST)


    pyramid = Pyramid()

    clock = pygame.time.Clock()

    running = True

    while running:

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


        glClear(
            GL_COLOR_BUFFER_BIT |
            GL_DEPTH_BUFFER_BIT
        )

        pyramid.draw()

        pygame.display.flip()


    pygame.quit()


main()