import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
 
pygame.init()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode([960, 600])
pygame.display.set_caption('Space Invaders')

imagen_de_fondo = pygame.image.load("fondomenu1.png").convert()
imagen_logo = pygame.image.load("logo1.png").convert()
imagen_com = pygame.image.load("comenzar.png").convert()
imagen_sal = pygame.image.load("salir.png").convert()
imagen_flch = pygame.image.load("flch.png").convert()


posicion1=[50,236]
posicion2=[50,330]
aux=[50,236]

def selec(x):


hecho = False
 
while not hecho:
    reloj.tick(60)
    pantalla.blit(imagen_flch, posicion1)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                pantalla.blit(imagen_flch, posicion1)
                aux=posicion1
            if evento.key == pygame.K_DOWN:
                pantalla.blit(imagen_flch, posicion2)
                aux=posicion2
            if evento.key == pygame.K_r:
            	if aux == posicion1:
                	import Space_invaders
                	hecho = True
                




    pantalla.blit(imagen_de_fondo, [0,0])
    pantalla.blit(imagen_logo, [25,25])
    pantalla.blit(imagen_com, [150,236])
    pantalla.blit(imagen_sal, [150,330])
    pantalla.blit(imagen_flch, aux)

    pygame.display.flip()
 
pygame.quit()
