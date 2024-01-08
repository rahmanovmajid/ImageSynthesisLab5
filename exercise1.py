from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Cone and Sphere parameters
cone_radius = 0.5
cone_height = 1.0
sphere_radius = 0.5

# Lighting parameters
light_position = (5.0, 5.0, 5.0, 1.0)
light_ambient = (0.2, 0.2, 0.2, 1.0)
light_diffuse = (1.0, 1.0, 1.0, 1.0)
light_specular = (1.0, 1.0, 1.0, 1.0)

# Material parameters
cone_material_ambient = (0.0, 0.5, 0.5, 1.0)
cone_material_diffuse = (0.0, 1.0, 1.0, 1.0)
cone_material_specular = (1.0, 1.0, 1.0, 1.0)
cone_material_shininess = 50.0

sphere_material_ambient = (0.5, 0.5, 0.0, 1.0)
sphere_material_diffuse = (1.0, 1.0, 0.0, 1.0)
sphere_material_specular = (1.0, 1.0, 1.0, 1.0)
sphere_material_shininess = 50.0

def draw_cone():
    glMaterialfv(GL_FRONT, GL_AMBIENT, cone_material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, cone_material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, cone_material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, cone_material_shininess)
    
    glutSolidCone(cone_radius, cone_height, 50, 50)

def draw_sphere():
    glMaterialfv(GL_FRONT, GL_AMBIENT, sphere_material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, sphere_material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, sphere_material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, sphere_material_shininess)
    
    glutSolidSphere(sphere_radius, 50, 50)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    
    draw_cone()
    draw_sphere()
    
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow("3D Scene with Cone and Sphere")
    glutReshapeWindow(800, 600)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
