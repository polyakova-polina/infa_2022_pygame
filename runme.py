import pygame
import random
from heli import Copter
from settings import *
from pathlib import Path


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("helicopter fly")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
copter = Copter()
all_sprites.add(copter)

background = pygame.image.load( Path(__file__).parent / "img" / "bckgnd" / bckgnd )#.convert()
background_rect = background.get_rect()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()