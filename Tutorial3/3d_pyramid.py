import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Window size
screen_width = 800
screen_height = 800


class Pyramid:

    # Original simple 3D coordinates
    vertices = [
        [-1, -1, -1],    # 0
        [-1, -1, 1],     # 1
        [1, -1, 1],    # 2
        [1, -1, -1],   # 3
        [0, 1, 0]       # 4 top
    ]

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

    # Bottom square
    base = (
        0, 1, 2, 3
    )


    def draw(self):

        # -------------------------
        # Draw triangular surfaces
        # -------------------------
        glBegin(GL_TRIANGLES)

        glColor3f(1.0, 0.5, 0.0)

        for triangle in self.triangles:

            for vertex in triangle:

                glVertex3fv(
                    self.vertices[vertex]
                )

        glEnd()


        # -------------------------
        # Draw bottom surface
        # -------------------------
        glBegin(GL_QUADS)

        glColor3f(1.0, 0.5, 0.0)

        for vertex in self.base:

            glVertex3fv(
                self.vertices[vertex]
            )

        glEnd()


        # -------------------------
        # Draw blue edges
        # -------------------------
        glLineWidth(4)

        glBegin(GL_LINES)

        glColor3f(0.0, 0.0, 1.0)

        for edge in self.edges:

            for vertex in edge:

                glVertex3fv(
                    self.vertices[vertex]
                )

        glEnd()



def main():

    pygame.init()

    display = (
        screen_width,
        screen_height
    )

    pygame.display.set_mode(
        display,
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption(
        "3D Pyramid"
    )


    # -------------------------
    # Projection
    # -------------------------
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluPerspective(
        45,
        screen_width / screen_height,
        0.1,
        50.0
    )


    # -------------------------
    # Camera
    # -------------------------
    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(

        4, 3, 6,     # Camera position

        0, 0, 0,     # Look at origin

        0, 1, 0      # Up direction
    )


    # Enable depth
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