import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
 
pygame.init()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode([960, 600])
pygame.display.set_caption('Space Invaders')

imagen_de_fondo = pygame.image.load("fondogameover.png").convert()


hecho = False
 
while not hecho:
    reloj.tick(60)
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_t:
                import Menu
                hecho = True


    pantalla.blit(imagen_de_fondo, [0,0])

    pygame.display.flip()
 
pygame.quit()