import pygame

class energia(pygame.sprite.Sprite):
    def __init__(self, posx, posy, nivel, derecha):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('Imagenes/rayoIzqN.png')
        self.poder = 25
        self.movimiento = -2
        
        if nivel == True:
            self.poder = 100
            if derecha == True:
                self.img = pygame.image.load('Imagenes/rayoDerS.png')
                self.movimiento = 2
            else:
                self.img = pygame.image.load('Imagenes/rayoIzqS.png')
        else:
            if derecha == True:
                self.img = pygame.image.load('Imagenes/rayoDerN.png')
                self.movimiento = 2
        
        self.rect = self.img.get_rect()
        
        self.rect.left = posx
        self.rect.top = posy

    def actualizar(self):
        self.rect.right += self.movimiento

    def dibujar(self, superficie):
        superficie.blit(self.img, self.rect)
