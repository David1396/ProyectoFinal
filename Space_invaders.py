import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
 
pygame.init()
pantalla = pygame.display.set_mode([960, 600])
pygame.display.set_caption('Space Invaders')
 
reloj = pygame.time.Clock()
sonido_laser = pygame.mixer.Sound("laser5.ogg")
posicion_base = [0, 0]

class alien():
    def __init__(self):
        # Posición de el alien
        self.x_alien = 0
        self.y_alien = 0
 
        # vector alien
        self.cambio_x_alien = 0
        self.cambio_y_alien = 0

        self.imagen=""
        
        # --- Métodos para la Clase ---
    def mover_alien(self):
        self.x_alien += self.cambio_x_alien
        self.y_alien += self.cambio_y_alien
            
    # Carga los aliens
    def dibujar_alien(self, pantalla):
        pantalla.blit(self.imagen, [self.x_alien, self.y_alien])


        
# Carga y sitúa los gráficos.
imagen_de_fondo = pygame.image.load("fondo1.png").convert()
imagen_nave = pygame.image.load("space1.png").convert()
imagen_nave.set_colorkey(NEGRO)

img_alien2 = pygame.image.load("alien2.png").convert()
img_alien3 = pygame.image.load("alien3.png").convert()
img_alien4 = pygame.image.load("alien4.png").convert()
img_alien5 = pygame.image.load("alien5.png").convert()

img_alien2.set_colorkey(NEGRO)
img_alien3.set_colorkey(NEGRO)
img_alien4.set_colorkey(NEGRO)
img_alien5.set_colorkey(NEGRO)

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
 
# Posición actual
x_coord = 400
y_coord = 500

#Clse de los aliens
ALIENS=alien()
ALIENS.x_alien=25
ALIENS.y_alien=95
ALIENS.cambio_x_alien=5
ALIENS.cambio_y_alien=0
ALIENS.imagen= img_alien2
 
ALIENS1=alien()
ALIENS1.x_alien=25
ALIENS1.y_alien=165
ALIENS1.cambio_x_alien=5
ALIENS1.cambio_y_alien=0
ALIENS1.imagen= img_alien3

ALIENS2=alien()
ALIENS2.x_alien=25
ALIENS2.y_alien=235
ALIENS2.cambio_x_alien=5
ALIENS2.cambio_y_alien=0
ALIENS2.imagen= img_alien4

ALIENS3=alien()
ALIENS3.x_alien=30
ALIENS3.y_alien=305
ALIENS3.cambio_x_alien=5
ALIENS3.cambio_y_alien=0
ALIENS3.imagen= img_alien5


hecho = False
 
while not hecho:
    reloj.tick(60)
    
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

    ALIENS.mover_alien()
    ALIENS.dibujar_alien(pantalla)

    ALIENS1.mover_alien()
    ALIENS1.dibujar_alien(pantalla)

    ALIENS2.mover_alien()
    ALIENS2.dibujar_alien(pantalla)

    ALIENS3.mover_alien()
    ALIENS3.dibujar_alien(pantalla)

    #Posicion Nave
    x = x_coord
    y = y_coord
     
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_nave, [x, y])
    
    pygame.display.flip()
 
pygame.quit()



