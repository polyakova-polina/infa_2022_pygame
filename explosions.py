import pygame
from settings import *


# взрыв вертолета
class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load( images_path / "explosion" / "explosion2.png" ).convert()
        self.image = pygame.transform.scale(img, (100, 100)) 
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

# создание границы
class Bound(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 1))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = pos
