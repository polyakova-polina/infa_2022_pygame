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
        self.speedx = gamespeed
        self.speedy = 0

        self.has_control = True

        self.boom = pygame.mixer.Sound( snd_path / "Chunky Explosion.mp3" )

        self.ammo = 100
        self.health = 100
        self.killed_enemies = 0

        self.name = "my_copter"

    # уничтожение вертолета со звуком
    def kill(self):
        super().kill()
        self.boom.play()
        self.rect.x = -100
        self.rect.y = -100
        self.health = 0

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
            self.rect.x += self.speedx
            if not ((self.rect.y+1) % 50):
                self.image = pygame.transform.flip(self.image, True, False)

class enemyCopter(pygame.sprite.Sprite):
    def __init__(self, pic, copter):
        Copter.__init__(self, pic)
        self.rect.centerx = WIDTH-10
        self.rect.bottom = random.randint(50, HEIGHT-50)
        self.speedx = -gamespeed
        self.speedy = gamespeed * random.randint(-1, 1)
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey(BLACK)

        self.name = "enemy_copter"

        self.copter = copter

        self.boom = pygame.mixer.Sound( snd_path / "DeathFlash.flac" )

    def kill(self):
        super().kill()
        self.boom.play()

    def update(self):
        if self.has_control:

            self.speedx = -gamespeed
            direct = self.copter.rect.y - self.rect.y
            direct = -1 if direct < 0 else 1
            self.speedy = gamespeed * direct

            self.rect.x += self.speedx
            self.rect.y += self.speedy

            self.has_control = False if self.rect.top < 0 else True # при врезании в потолок теряем управление и по факту падаем на землю

            self.rect.top = 0 if self.rect.top < 0 else self.rect.top
            if self.rect.left < 0:
                self.kill()

            self.rect.bottom = HEIGHT if self.rect.bottom > HEIGHT else self.rect.bottom

        else:
            self.rect.y += 10 # потеряли управление - падаем
            self.rect.x += self.speedx
            if not ((self.rect.y+1) % 50):
                self.image = pygame.transform.flip(self.image, True, False)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction=1):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (10, 5) )
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.midright = (x, y)
        self.dir = direction

        self.speedx = gamespeed*2*self.dir

        self.name = "bullet"

    def update(self):
        self.rect.x += gamespeed*2*self.dir
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()

class gameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load( images_path / "game over.png" ).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0

    def update(self):
        pass
