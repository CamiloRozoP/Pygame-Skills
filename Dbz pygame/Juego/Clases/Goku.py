import pygame
from Clases import Energia

class goku(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        
        self.ancho = ancho
        self.alto = alto
        
        self.img = pygame.image.load('Imagenes/trans1.png')

        self.rect = self.img.get_rect()
        self.sprite = 0
        self.vida = 100
        self.puntos = 0
        self.trans = 0
        self.proceso = 0
        self.danoRecibido = 4
        self.poderAtaque = 10
        self.poderSs = 0

        self.rect.left = 0
        self.rect.centery = alto / 2        

        self.disparos = []
        
        self.sonidoAtaque = pygame.mixer.Sound("Sonidos/Ataque.wav")
        self.sonidoTransformacion = pygame.mixer.Sound("Sonidos/TransformacionSs.wav")
        self.sonidoSalto = pygame.mixer.Sound("Sonidos/Salto.wav")
        self.sonidoSalto.set_volume(0.1)

    def procesoTransformacion(self):
        #proceso de transformacion
        if self.trans == 5:
            self.sonidoTransformacion.play()
                
        if self.trans > 0 and self.trans < 8 and self.proceso > 39:
            self.transformandose(self.trans - 1)
            self.trans += 1
            self.proceso = 0

        if self.trans == 5 and self.proceso == 0:
            self.rect.left -= 10
            self.rect.top -= 20
        
        if self.trans == 8 and self.proceso == 0:
            self.rect.left += 10
            self.rect.top += 20
        
        if self.trans == 0:
            self.danoRecibido = 4
            self.poderAtaque = 10
            self.proceso = 0
        else:
            self.proceso += 1
            if self.trans > 7:
                self.poderSs -= 1
            if self.poderSs == 0:
                self.trans = 0
                self.transformandose(0)

    def controles(self, accion):
        #controles
        if accion == 'arriba' and self.rect.top > 80:
            self.sonidoSalto.play()
            self.rect.top -= 10
            if self.trans == 0:
                if self.sprite == 0 or self.sprite == 2 or self.sprite == 4:
                    self.sonidoSalto.play()
                    self.normal(0)
                    self.sprite = 0
                else:
                    self.normal(1)
                    self.sprite = 1
            if self.trans > 7:
                if self.sprite == 0 or self.sprite == 2 or self.sprite == 4:
                    self.transformado(0)
                    self.sprite = 0
                else:
                    self.transformado(1)
                    self.sprite = 1

        if accion == 'abajo' and self.rect.bottom < self.alto:
            self.sonidoSalto.play()
            self.rect.bottom += 10
            if self.trans == 0:
                if self.sprite == 0 or self.sprite == 2 or self.sprite == 4:
                    self.normal(2)
                    self.sprite = 2
                else:
                    self.normal(3)
                    self.sprite = 3
            if self.trans > 7:
                if self.sprite == 0 or self.sprite == 2 or self.sprite == 4:
                    self.transformado(2)
                    self.sprite = 2
                else:
                    self.transformado(3)
                    self.sprite = 3
                
        if accion == 'izquierda' and self.rect.left > 0:
            self.sonidoSalto.play()
            self.sprite = 5
            self.rect.left -= 10
            if self.trans == 0:
                self.normal(5)
            if self.trans > 7:
                self.transformado(5)

        if accion == 'derecha' and self.rect.right < self.ancho - 20:
            self.sonidoSalto.play()
            self.sprite = 4
            self.rect.right += 10
            if self.trans == 0:
                self.normal(4)
            if self.trans > 7:
                self.transformado(4)

        if accion == 'energia':
            self.sonidoAtaque.play()
            if self.sprite == 0 or self.sprite == 2 or self.sprite == 4:
                if self.trans == 0:
                    self.disparos.append(Energia.energia(self.rect.right, self.rect.top + 10, False, True))
                    self.normal(7)
                if self.trans > 7:
                    self.disparos.append(Energia.energia(self.rect.right, self.rect.top, True, True))
                    self.transformado(7)
            else:
                if self.trans == 0:
                    self.disparos.append(Energia.energia(self.rect.left, self.rect.top + 10, False, False))
                    self.normal(8)
                if self.trans > 7:
                    self.disparos.append(Energia.energia(self.rect.left, self.rect.top, True, False))
                    self.transformado(8)
            
        
        if accion == 'trans':
            if self.poderSs >= 10000:
                self.proceso = 40
                self.danoRecibido = 1
                self.poderAtaque = 25
                if self.trans == 0:
                    self.trans += 1
            else:
                self.trans = 0;
                self.transformandose(0)
                self.proceso = 0

    def normal(self,sprite): #imagenes normal
        imgN = ['arrDerN', 'arrIzqN', 'abDerN', 'abIzqN', 'derN', 'izqN'
                , 'golpeN', 'ataqueDerN', 'ataqueIzqN', 'muertoN']
        self.img = pygame.image.load('Imagenes/' + imgN[sprite] + '.png')
    
    def transformado(self,sprite): #imagenes transformado
        imgS = ['arrDerS', 'arrIzqS', 'abDerS', 'abIzqS', 'derS' , 'izqS'
                , 'golpeS', 'ataqueDerS', 'ataqueIzqS', 'muertoS']
        self.img = pygame.image.load('Imagenes/' + imgS[sprite] + '.png')
    
    def transformandose(self,sprite): #imagenes proceso transformacion
        imgT = ['trans1', 'trans2', 'trans3', 'trans4'
                , 'trans5', 'trans6', 'trans7']
        self.img = pygame.image.load('Imagenes/' + imgT[sprite] + '.png')
            
    def actualizar(self,accion):
        self.procesoTransformacion()
        self.controles(accion)
        
    def dibujar(self, superficie):
        self.textoSayayin = pygame.font.SysFont("Arial", 30).render(
                "Poder Super Sayayin: " + str(self.poderSs / 100) + "%",0,(255, 255, 255))
        
        self.textoPuntos = pygame.font.SysFont("Arial", 30).render(
                "Puntos: " + str(self.puntos),0,(255, 255, 255))
        
        self.textoVida = pygame.font.SysFont("Arial", 30).render(
                "Vida: " + str(self.vida),0,(255, 255, 255))
        
        superficie.blit(self.img, self.rect)
        superficie.blit(self.textoPuntos,(10,10))
        superficie.blit(self.textoVida,(10,40))
        superficie.blit(self.textoSayayin,(self.ancho - 500,10))
