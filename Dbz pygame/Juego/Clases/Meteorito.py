import pygame
from random import randint

class meteorito(pygame.sprite.Sprite):
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)

        self.img = pygame.image.load('Imagenes/rayoE.png')
        self.poder = 100
        self.rect = self.img.get_rect()

        self.ancho = ancho
        self.rect.right = ancho
        self.rect.bottom = randint(80 + self.rect.height, alto - 40)
        
        self.movimiento = randint(-5, -2)

    def actualizar(self):
        if self.rect.left < 0:
            self.rect.right = self.ancho
        else:
            self.rect.left += self.movimiento
    
    def dibujar(self, superficie):
        superficie.blit(self.img, self.rect)
