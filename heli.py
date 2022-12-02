import pygame
from settings import *
import random


class Copter(pygame.sprite.Sprite):
    def __init__(self, pic):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load( images_path / pic ).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 10
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0

        self.has_control = True

    def update(self):
        if self.has_control:
            keystate = pygame.key.get_pressed()

            self.speedx = -gamespeed if keystate[pygame.K_LEFT] else self.speedx            
            self.speedx = gamespeed if keystate[pygame.K_RIGHT] else self.speedx
            self.speedy = -gamespeed if keystate[pygame.K_UP] else self.speedy
            self.speedy = gamespeed if keystate[pygame.K_DOWN] else self.speedy

            self.rect.x += self.speedx
            self.rect.y += self.speedy

            self.has_control = False if self.rect.top < 0 else True # при врезании в потолок теряем управление и по факту падаем на землю

            #self.rect.top = 0 if self.rect.top < 0 else self.rect.top
            self.rect.left = 0 if self.rect.left < 0 else self.rect.left
            self.rect.right = WIDTH if self.rect.right > WIDTH else self.rect.right
            self.rect.bottom = HEIGHT if self.rect.bottom > HEIGHT else self.rect.bottom

        else:
            self.rect.y += 10 # потеряли управление - падаем
            if not ((self.rect.y+1) % 50):
                self.image = pygame.transform.flip(self.image, True, False)

class enemyCopter(Copter):
    def __init__(self, pic):
        Copter.__init__(self, pic)
        self.rect.centerx = WIDTH-10
        self.rect.bottom = random.randint(50, HEIGHT-50)
        self.speedx = -gamespeed
        self.speedy = gamespeed * random.randint(-1, 1)
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey(BLACK)
    def update(self):
        if self.has_control:

            self.speedx = -gamespeed
            self.speedy = gamespeed * random.randint(-2, 2)

            self.rect.x += self.speedx
            self.rect.y += self.speedy

            self.has_control = False if self.rect.top < 0 else True # при врезании в потолок теряем управление и по факту падаем на землю

            self.rect.top = 0 if self.rect.top < 0 else self.rect.top
            if self.rect.left < 0:
                self.kill()

            self.rect.bottom = HEIGHT if self.rect.bottom > HEIGHT else self.rect.bottom

        else:
            self.rect.y += 10 # потеряли управление - падаем
            if not ((self.rect.y+1) % 50):
                self.image = pygame.transform.flip(self.image, True, False)