import pygame
import random
from settings import *
from pathlib import Path


class Copter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 40))
        self.image = pygame.image.load( images_path / "less_til_heli.png" ).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 10
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0

    def update(self):
        keystate = pygame.key.get_pressed()

        self.speedx = -gamespeed if keystate[pygame.K_LEFT] else self.speedx            
        self.speedx = gamespeed if keystate[pygame.K_RIGHT] else self.speedx
        self.speedy = -gamespeed if keystate[pygame.K_UP] else self.speedy
        self.speedy = gamespeed if keystate[pygame.K_DOWN] else self.speedy

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.left = 0 if self.rect.left < 0 else self.rect.left
        self.rect.right = WIDTH if self.rect.right > WIDTH else self.rect.right
        self.rect.bottom = HEIGHT if self.rect.bottom > HEIGHT else self.rect.bottom
        