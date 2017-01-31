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
        if self.x_alien <= 860 and self.x_alien>= 25:
            self.x_alien += self.cambio_x_alien
            #self.y_alien += self.cambio_y_alien
            if self.x_alien == 860 or self.x_alien == 25:
                self.cambio_x_alien = self.cambio_x_alien*(-1)

            
    # Carga los aliens
    def dibujar_alien(self, pantalla):
        pantalla.blit(self.imagen, [self.x_alien, self.y_alien])

class superalien():
    def __init__(self):
        self.x_alien = 0
        self.cambio_x_alien = 0

        self.imagen=""
        
    # --- Métodos para la Clase ---
    def mover_superalien(self):
        if self.x_alien <= 1960 and self.x_alien>= -1000:
            self.x_alien += self.cambio_x_alien
            if self.x_alien == -1000 or self.x_alien == 1960:
                self.cambio_x_alien = self.cambio_x_alien*(-1)

            
    # Carga los aliens
    def dibujar_superalien(self, pantalla):
        pantalla.blit(self.imagen, [self.x_alien, self.y_alien])

def acciones_aliens():
    ALIENS0.mover_superalien()
    ALIENS0.dibujar_superalien(pantalla)

    ALIENS.mover_alien()
    ALIENS.dibujar_alien(pantalla)

    ALIENS1.mover_alien()
    ALIENS1.dibujar_alien(pantalla)

    ALIENS2.mover_alien()
    ALIENS2.dibujar_alien(pantalla)

    ALIENS3.mover_alien()
    ALIENS3.dibujar_alien(pantalla)

    ALIENS4.mover_alien()
    ALIENS4.dibujar_alien(pantalla)

    ALIENS5.mover_alien()
    ALIENS5.dibujar_alien(pantalla)

    ALIENS6.mover_alien()
    ALIENS6.dibujar_alien(pantalla)

    ALIENS7.mover_alien()
    ALIENS7.dibujar_alien(pantalla)

    ALIENS8.mover_alien()
    ALIENS8.dibujar_alien(pantalla)

    ALIENS9.mover_alien()
    ALIENS9.dibujar_alien(pantalla)

    ALIENS10.mover_alien()
    ALIENS10.dibujar_alien(pantalla)

    ALIENS11.mover_alien()
    ALIENS11.dibujar_alien(pantalla)

    ALIENS12.mover_alien()
    ALIENS12.dibujar_alien(pantalla)

    ALIENS13.mover_alien()
    ALIENS13.dibujar_alien(pantalla)

    ALIENS14.mover_alien()
    ALIENS14.dibujar_alien(pantalla)

    ALIENS15.mover_alien()
    ALIENS15.dibujar_alien(pantalla)

    ALIENS16.mover_alien()
    ALIENS16.dibujar_alien(pantalla)

    ALIENS17.mover_alien()
    ALIENS17.dibujar_alien(pantalla)

    ALIENS18.mover_alien()
    ALIENS18.dibujar_alien(pantalla)

    ALIENS19.mover_alien()
    ALIENS19.dibujar_alien(pantalla)

    ALIENS20.mover_alien()
    ALIENS20.dibujar_alien(pantalla)

    ALIENS21.mover_alien()
    ALIENS21.dibujar_alien(pantalla)

    ALIENS22.mover_alien()
    ALIENS22.dibujar_alien(pantalla)

    ALIENS23.mover_alien()
    ALIENS23.dibujar_alien(pantalla)

    ALIENS24.mover_alien()
    ALIENS24.dibujar_alien(pantalla)

    ALIENS25.mover_alien()
    ALIENS25.dibujar_alien(pantalla)

    ALIENS26.mover_alien()
    ALIENS26.dibujar_alien(pantalla)

    ALIENS27.mover_alien()
    ALIENS27.dibujar_alien(pantalla)

    ALIENS28.mover_alien()
    ALIENS28.dibujar_alien(pantalla)

    ALIENS29.mover_alien()
    ALIENS29.dibujar_alien(pantalla)

    ALIENS30.mover_alien()
    ALIENS30.dibujar_alien(pantalla)

    ALIENS31.mover_alien()
    ALIENS31.dibujar_alien(pantalla)

    ALIENS32.mover_alien()
    ALIENS32.dibujar_alien(pantalla)

    ALIENS33.mover_alien()
    ALIENS33.dibujar_alien(pantalla)

    ALIENS34.mover_alien()
    ALIENS34.dibujar_alien(pantalla)

    ALIENS35.mover_alien()
    ALIENS35.dibujar_alien(pantalla)
        
# Carga y sitúa los gráficos.
imagen_de_fondo = pygame.image.load("fondo1.png").convert()
imagen_nave = pygame.image.load("space1.png").convert()
imagen_nave.set_colorkey(NEGRO)

img_alien2 = pygame.image.load("alien2.png").convert()
img_alien3 = pygame.image.load("alien3.png").convert()
img_alien4 = pygame.image.load("alien4.png").convert()
img_alien5 = pygame.image.load("alien5.png").convert()
img_superalien = pygame.image.load("superalien.png").convert()

img_alien2.set_colorkey(NEGRO)
img_alien3.set_colorkey(NEGRO)
img_alien4.set_colorkey(NEGRO)
img_alien5.set_colorkey(NEGRO)
img_superalien.set_colorkey(NEGRO)

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
 
# Posición actual
x_coord = 444
y_coord = 500

#Clase de los aliens----------------------------------------------------
ALIENS0=superalien()
ALIENS0.x_alien=-1000
ALIENS0.y_alien=25
ALIENS0.cambio_x_alien=10
ALIENS0.cambio_y_alien=0
ALIENS0.imagen= img_superalien
#---------------------------------------
#--------   Primera columna
ALIENS=alien()
ALIENS.x_alien=25
ALIENS.y_alien=95
ALIENS.cambio_x_alien=2.5
ALIENS.cambio_y_alien=0
ALIENS.imagen= img_alien2
 
ALIENS1=alien()
ALIENS1.x_alien=25
ALIENS1.y_alien=165
ALIENS1.cambio_x_alien=2.5
ALIENS1.cambio_y_alien=0
ALIENS1.imagen= img_alien3

ALIENS2=alien()
ALIENS2.x_alien=25
ALIENS2.y_alien=235
ALIENS2.cambio_x_alien=2.5
ALIENS2.cambio_y_alien=0
ALIENS2.imagen= img_alien4

ALIENS3=alien()
ALIENS3.x_alien=25
ALIENS3.y_alien=305
ALIENS3.cambio_x_alien=2.5
ALIENS3.cambio_y_alien=0
ALIENS3.imagen= img_alien5
#------------------------------ Segunda columna
ALIENS4=alien()
ALIENS4.x_alien=115
ALIENS4.y_alien=95
ALIENS4.cambio_x_alien=2.5
ALIENS4.cambio_y_alien=0
ALIENS4.imagen= img_alien2
 
ALIENS5=alien()
ALIENS5.x_alien=115
ALIENS5.y_alien=165
ALIENS5.cambio_x_alien=2.5
ALIENS5.cambio_y_alien=0
ALIENS5.imagen= img_alien3

ALIENS6=alien()
ALIENS6.x_alien=115
ALIENS6.y_alien=235
ALIENS6.cambio_x_alien=2.5
ALIENS6.cambio_y_alien=0
ALIENS6.imagen= img_alien4

ALIENS7=alien()
ALIENS7.x_alien=115
ALIENS7.y_alien=305
ALIENS7.cambio_x_alien=2.5
ALIENS7.cambio_y_alien=0
ALIENS7.imagen= img_alien5
#------------------------------     tercera columna
ALIENS8=alien()
ALIENS8.x_alien=205
ALIENS8.y_alien=95
ALIENS8.cambio_x_alien=2.5
ALIENS8.cambio_y_alien=0
ALIENS8.imagen= img_alien2
 
ALIENS9=alien()
ALIENS9.x_alien=205
ALIENS9.y_alien=165
ALIENS9.cambio_x_alien=2.5
ALIENS9.cambio_y_alien=0
ALIENS9.imagen= img_alien3

ALIENS10=alien()
ALIENS10.x_alien=205
ALIENS10.y_alien=235
ALIENS10.cambio_x_alien=2.5
ALIENS10.cambio_y_alien=0
ALIENS10.imagen= img_alien4

ALIENS11=alien()
ALIENS11.x_alien=205
ALIENS11.y_alien=305
ALIENS11.cambio_x_alien=2.5
ALIENS11.cambio_y_alien=0
ALIENS11.imagen= img_alien5
#------------------------------          cuarta columna
ALIENS12=alien()
ALIENS12.x_alien=295
ALIENS12.y_alien=95
ALIENS12.cambio_x_alien=2.5
ALIENS12.cambio_y_alien=0
ALIENS12.imagen= img_alien2
 
ALIENS13=alien()
ALIENS13.x_alien=295
ALIENS13.y_alien=165
ALIENS13.cambio_x_alien=2.5
ALIENS13.cambio_y_alien=0
ALIENS13.imagen= img_alien3

ALIENS14=alien()
ALIENS14.x_alien=295
ALIENS14.y_alien=235
ALIENS14.cambio_x_alien=2.5
ALIENS14.cambio_y_alien=0
ALIENS14.imagen= img_alien4

ALIENS15=alien()
ALIENS15.x_alien=295
ALIENS15.y_alien=305
ALIENS15.cambio_x_alien=2.5
ALIENS15.cambio_y_alien=0
ALIENS15.imagen= img_alien5
#------------------------------          quinta columna
ALIENS16=alien()
ALIENS16.x_alien=385
ALIENS16.y_alien=95
ALIENS16.cambio_x_alien=2.5
ALIENS16.cambio_y_alien=0
ALIENS16.imagen= img_alien2
 
ALIENS17=alien()
ALIENS17.x_alien=385
ALIENS17.y_alien=165
ALIENS17.cambio_x_alien=2.5
ALIENS17.cambio_y_alien=0
ALIENS17.imagen= img_alien3

ALIENS18=alien()
ALIENS18.x_alien=385
ALIENS18.y_alien=235
ALIENS18.cambio_x_alien=2.5
ALIENS18.cambio_y_alien=0
ALIENS18.imagen= img_alien4

ALIENS19=alien()
ALIENS19.x_alien=385
ALIENS19.y_alien=305
ALIENS19.cambio_x_alien=2.5
ALIENS19.cambio_y_alien=0
ALIENS19.imagen= img_alien5
#------------------------------      sexta columna
ALIENS20=alien()
ALIENS20.x_alien=475
ALIENS20.y_alien=95
ALIENS20.cambio_x_alien=2.5
ALIENS20.cambio_y_alien=0
ALIENS20.imagen= img_alien2
 
ALIENS21=alien()
ALIENS21.x_alien=475
ALIENS21.y_alien=165
ALIENS21.cambio_x_alien=2.5
ALIENS21.cambio_y_alien=0
ALIENS21.imagen= img_alien3

ALIENS22=alien()
ALIENS22.x_alien=475
ALIENS22.y_alien=235
ALIENS22.cambio_x_alien=2.5
ALIENS22.cambio_y_alien=0
ALIENS22.imagen= img_alien4

ALIENS23=alien()
ALIENS23.x_alien=475
ALIENS23.y_alien=305
ALIENS23.cambio_x_alien=2.5
ALIENS23.cambio_y_alien=0
ALIENS23.imagen= img_alien5
#------------------------------     septima columna
ALIENS24=alien()
ALIENS24.x_alien=565
ALIENS24.y_alien=95
ALIENS24.cambio_x_alien=2.5
ALIENS24.cambio_y_alien=0
ALIENS24.imagen= img_alien2
 
ALIENS25=alien()
ALIENS25.x_alien=565
ALIENS25.y_alien=165
ALIENS25.cambio_x_alien=2.5
ALIENS25.cambio_y_alien=0
ALIENS25.imagen= img_alien3

ALIENS26=alien()
ALIENS26.x_alien=565
ALIENS26.y_alien=235
ALIENS26.cambio_x_alien=2.5
ALIENS26.cambio_y_alien=0
ALIENS26.imagen= img_alien4

ALIENS27=alien()
ALIENS27.x_alien=565
ALIENS27.y_alien=305
ALIENS27.cambio_x_alien=2.5
ALIENS27.cambio_y_alien=0
ALIENS27.imagen= img_alien5
#------------------------------          octava columna
ALIENS28=alien()
ALIENS28.x_alien=655
ALIENS28.y_alien=95
ALIENS28.cambio_x_alien=2.5
ALIENS28.cambio_y_alien=0
ALIENS28.imagen= img_alien2
 
ALIENS29=alien()
ALIENS29.x_alien=655
ALIENS29.y_alien=165
ALIENS29.cambio_x_alien=2.5
ALIENS29.cambio_y_alien=0
ALIENS29.imagen= img_alien3

ALIENS30=alien()
ALIENS30.x_alien=655
ALIENS30.y_alien=235
ALIENS30.cambio_x_alien=2.5
ALIENS30.cambio_y_alien=0
ALIENS30.imagen= img_alien4

ALIENS31=alien()
ALIENS31.x_alien=655
ALIENS31.y_alien=305
ALIENS31.cambio_x_alien=2.5
ALIENS31.cambio_y_alien=0
ALIENS31.imagen= img_alien5
#------------------------------          novena columna
ALIENS32=alien()
ALIENS32.x_alien=745
ALIENS32.y_alien=95
ALIENS32.cambio_x_alien=2.5
ALIENS32.cambio_y_alien=0
ALIENS32.imagen= img_alien2
 
ALIENS33=alien()
ALIENS33.x_alien=745
ALIENS33.y_alien=165
ALIENS33.cambio_x_alien=2.5
ALIENS33.cambio_y_alien=0
ALIENS33.imagen= img_alien3

ALIENS34=alien()
ALIENS34.x_alien=745
ALIENS34.y_alien=235
ALIENS34.cambio_x_alien=2.5
ALIENS34.cambio_y_alien=0
ALIENS34.imagen= img_alien4

ALIENS35=alien()
ALIENS35.x_alien=745
ALIENS35.y_alien=305
ALIENS35.cambio_x_alien=2.5
ALIENS35.cambio_y_alien=0
ALIENS35.imagen= img_alien5


#------------------------------------------------------------------------
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

    acciones_aliens()

    #Posicion Nave
    x = x_coord
    y = y_coord
     
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_nave, [x, y])
    
    pygame.display.flip()
 
pygame.quit()



