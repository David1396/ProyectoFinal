import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
 
pygame.init()
pantalla = pygame.display.set_mode([960, 600])
pygame.display.set_caption('Space Invaders')
 
reloj = pygame.time.Clock()
sonido_laser = pygame.mixer.Sound("laser5.ogg")
posicion_base = [0, 0]
 
# Carga y sitúa los gráficos.
imagen_de_fondo = pygame.image.load("fondo1.png").convert()
imagen_nave = pygame.image.load("space1.png").convert()

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
 
# Posición actual
x_coord = 400
y_coord = 500
 
hecho = False
 
while not hecho:
    reloj.tick(10)
     
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
            # El usuario pulsa una tecla
        if evento.type == pygame.KEYDOWN:
            # Resuelve que ha sido una tecla de flecha, por lo que
            # ajusta la velocidad
            if evento.key == pygame.K_LEFT:
                x_speed = -10
            if evento.key == pygame.K_RIGHT:
                x_speed = 10
            if evento.key == pygame.K_SPACE:
                sonido_laser.play()
     
        # El usuario suelta la tecla
        if evento.type == pygame.KEYUP:
            # Si se trata de una tecla de flecha, devuelve el vector a cero
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
            
     
    # Mueve el objeto de acuerdo a la velocidad del vector.
    x_coord += x_speed 
             
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, posicion_base)
 
    # Obtiene la posición actual del ratón. Devuelve ésta como
    # una lista de dos números.
    #posicion_nave = pygame.mouse.get_pos()
    x = x_coord
    y = y_coord
     
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_nave, [x, y])
     
    pygame.display.flip()
    reloj.tick(60)
 
pygame.quit()



