import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
 
pygame.init()
pantalla = pygame.display.set_mode([960, 600])
pygame.display.set_caption('Space Invaders')

imagen_de_fondo = pygame.image.load("fondomenu1.png").convert()
imagen_logo = pygame.image.load("logo.png").convert()


hecho = False
 
while not hecho:
    reloj.tick(60)
    pantalla.blit(imagen_de_fondo, [0,0])
    pantalla.blit(imagen_logo, [25,25])
    pygame.display.flip()
 
pygame.quit()
