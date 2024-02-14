import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)

def draw_triangle():
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    glEnable(GL_CULL_FACE)   # Enable face culling
    glCullFace(GL_BACK)      # Specify culling of back faces

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rotation_speed = 0.2
    zoom_speed = 0.1
    rotation = [0, 0]
    zoom = 0
    prev_mouse_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                prev_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                prev_mouse_pos = None

        if prev_mouse_pos is not None and pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
            current_mouse_pos = pygame.mouse.get_pos()
            delta_x = current_mouse_pos[0] - prev_mouse_pos[0]
            delta_y = current_mouse_pos[1] - prev_mouse_pos[1]
            rotation[0] += delta_y * rotation_speed
            rotation[1] += delta_x * rotation_speed
            prev_mouse_pos = current_mouse_pos

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        glTranslatef(0.0, 0.0, zoom)
        
        draw_triangle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
