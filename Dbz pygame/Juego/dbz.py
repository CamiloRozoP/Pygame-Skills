import pygame,sys
from pygame.locals import *
from random import randint
from Clases import Goku
from Clases import Meteorito

#variables globales
ancho = 1000
alto = 680

def Dbz():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("DRAGON BALL Z")
    jugando = True
    pausa = False
    
    fondos = ['a','b','c','d','e','f','g']
    ImagenFondo = pygame.image.load('Fondos/' + fondos[randint(1, 8) - 2] + '.png')
    ImagenDatos = pygame.image.load('Fondos/datos.png')
    estado = "JUGANDO"

    sonidoExplosion = pygame.mixer.Sound("Sonidos/Explosion.wav")    
    sonidoExplosionFinal = pygame.mixer.Sound('Sonidos/ExplosionFinal.wav')
    pygame.mixer.music.load('Sonidos/Fondo.mp3')
    pygame.mixer.music.play(10000)

    listaMeteoritos = []
    goku = Goku.goku(ancho, alto)
    for x in range(1, 6):
        listaMeteoritos.append(Meteorito.meteorito(ancho, alto))

    while True:
        ventana.blit(ImagenFondo,(0,80))
        ventana.blit(ImagenDatos,(0,0))
        textoEstado = pygame.font.SysFont("Arial", 30).render(estado,0,(255,255,255))
        ventana.blit(textoEstado,(ancho - 500,40))
        goku.dibujar(ventana)
        if pausa == False:
            if jugando == True:
                #controles
                if pygame.key.get_pressed()[pygame.K_UP]:
                    goku.actualizar('arriba')
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    goku.actualizar('abajo')
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    goku.actualizar('izquierda')
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    goku.actualizar('derecha')
                
                for meteorito in listaMeteoritos: #recorre los meteoritos
                    meteorito.dibujar(ventana)
                    meteorito.actualizar()

                    if goku.rect.colliderect(meteorito.rect): #colision del personaje y un meteoritos
                        goku.vida -= goku.danoRecibido
                        meteorito.rect.right = ancho
                        listaMeteoritos.append(Meteorito.meteorito(ancho, alto))
                        if goku.trans == 0:
                            goku.normal(6)
                        else:
                            goku.transformado(6)
                        sonidoExplosion.play()

                    if len(goku.disparos) > 0:
                        for energia in goku.disparos: #recorre ataque del personaje
                            energia.actualizar()
                            energia.dibujar(ventana)
                            if energia.rect.left < 0 or energia.rect.right > ancho:
                                goku.disparos.remove(energia)
                            else:
                                if energia.rect.colliderect(meteorito.rect):
                                    meteorito.poder -= energia.poder
                                    goku.disparos.remove(energia)
                                    if meteorito.poder < 1:
                                        goku.puntos += 100
                                        if goku.trans == 0:
                                            if goku.poderSs < 10000:
                                               goku.poderSs += 500
                                               if goku.poderSs > 10000:
                                                   goku.poderSs = 10000
                                        if len(listaMeteoritos) == 4:
                                            meteorito.rect.right = ancho
                                            meteorito.rect.bottom = randint(80 + meteorito.rect.height, alto - 40)
                                            meteorito.poder = 100
                                        else:
                                            listaMeteoritos.remove(meteorito)

                if goku.poderSs == 10000:
                    estado = "OPRIMA 'a' PARA TRANSFORMARSE"
                else:
                    estado = "JUGANDO"

                goku.actualizar('')
                if goku.vida <= 0:
                    sonidoExplosionFinal.play()
                    goku.vida = 0
                    jugando = False
                    goku.rect.left += 40

            else:
                estado = "GAMEOVER"
                if goku.trans == 0:
                    goku.normal(9)
                else:
                    goku.transformado(9)

                if goku.rect.right > ancho:
                    goku.rect.right = ancho - 40
                    
                pygame.mixer.music.stop()
                
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()                
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_r:
                    Dbz()
                if jugando == True:
                    if evento.key == K_s and pausa == False:
                        goku.actualizar('energia')
                    if evento.key == K_a and pausa == False:
                        goku.actualizar('trans')
                    if evento.key == K_SPACE:
                        if pausa == False:
                            pausa = True
                            estado = "PAUSA"
                            pygame.mixer.music.pause()
                        else:
                            pausa = False
                            estado = "JUGANDO"
                            pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.fadeout(3000)
                    
        
        pygame.display.update()

Dbz() #ejecutar juego
