from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Draw eight symmetric points around the centre (xc, yc).
def plotCirclePoints(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)  # Second octant
    glVertex2f(xc + y, yc + x)  # First octant
    glVertex2f(xc - x, yc + y)  # Third octant
    glVertex2f(xc - y, yc + x)  # Fourth octant
    glVertex2f(xc - y, yc - x)  # Fifth octant
    glVertex2f(xc - x, yc - y)  # Sixth octant
    glVertex2f(xc + x, yc - y)  # Seventh octant
    glVertex2f(xc + y, yc - x)  # Eighth octant

# Draw a circle with centre (xc, yc) and radius R.
def drawCircle(xc, yc, R):
    x, y = 0, R                 # Start at the topmost point.
    h = 1 - R                   # Initial decision parameter.

    glBegin(GL_POINTS)

    # Draw the starting point and its symmetric points.
    plotCirclePoints(xc, yc, x, y)

    while y > x:                # Continue towards the line x = y.
        if h < 0:               # Choose East: move right.
            h = h + 2*x + 3
        else:                   # Choose South-East: move right and down.
            h = h + 2*(x-y) + 5
            y = y - 1           # Move down by one unit.

        x = x + 1               # Move right in both cases.

        # Draw the new point and its seven symmetric points.
        plotCirclePoints(xc, yc, x, y)

    glEnd()

def display():
    # Clear the drawing area.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set the drawing colour to black.
    glColor3f(0.0, 0.0, 0.0)

    # Draw a circle centred at (250, 250) with radius 150.
    drawCircle(250, 250, 150)

    # Wait until the drawing finishes.
    glFinish()

    # Read the drawing from the back buffer.
    glReadBuffer(GL_BACK)

    # Store pixel rows without adding extra bytes between them.
    glPixelStorei(GL_PACK_ALIGNMENT, 1)

    # Capture the entire 500 × 500 drawing.
    pixels = glReadPixels(
        0, 0, 500, 500, GL_RGB, GL_UNSIGNED_BYTE
    )

    # Convert the captured pixels into an image.
    image = Image.frombytes("RGB", (500, 500), pixels)

    # Flip the image to match OpenGL's upward y-direction.
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    # Present the completed drawing.
    glutSwapBuffers()

    # Opens the image natively in Windows Photo Viewer
    image.show()

# Initialise GLUT.
glutInit([])

# Enable double buffering, RGB colour, and a depth buffer.
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

# Set the window size.
glutInitWindowSize(500, 500)

# Create an OpenGL window.
window = glutCreateWindow(b"Bresenham Circle Drawing")

# Register the drawing function.
glutDisplayFunc(display)

# Set the background colour to white.
glClearColor(1.0, 1.0, 1.0, 1.0)

# Use the full window, starting at its bottom-left corner.
glViewport(0, 0, 500, 500)

# Select and reset the projection matrix.
glMatrixMode(GL_PROJECTION)
glLoadIdentity()

# Set x and y coordinates from 0 to 500.
gluOrtho2D(0, 500, 0, 500)

# Reset object transformations.
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Render once and show the output.
display()

# Close the window.
glutDestroyWindow(window)