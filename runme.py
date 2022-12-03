import pygame
import random
from heli import Copter, enemyCopter
from explosions import *
from settings import *
from pathlib import Path


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("helicopter fly")
clock = pygame.time.Clock()

background = pygame.image.load( Path(__file__).parent / "img" / "bckgnd" / bckgnd )#.convert()
background_rect = background.get_rect()

explosion = Explosion()
copter = Copter(heli_pic) # наш вертолет
bounds = [Bound(HEIGHT-1), Bound(0)] # граница по земле и по небу
all_sprites = pygame.sprite.Group()
all_sprites.add(copter)

enemyCopters = []

# Цикл игры
running = 1
while running:
    running += 1

    if not (running % 200):
        enemy = enemyCopter("helicopter_1.png")
        enemyCopters.append(enemy)
        all_sprites.add(enemy)
        #print(running, all_sprites.sprites())

    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = 0
        
        # ЛКМ - перезапуск игры
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #  левая кнопка мыши
                running = 1
                copter = Copter(heli_pic) # наш вертолет
                all_sprites.empty()
                all_sprites.add(copter)
                enemyCopters = []

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    heli_crash = pygame.sprite.spritecollide(copter, enemyCopters, False)
    if heli_crash:
        for hit in heli_crash:
            hit.kill()
            copter.kill()

            explosion.rect.bottom = copter.rect.bottom
            explosion.rect.left = copter.rect.left
            all_sprites.add(explosion)

    # Проверка, врезания в землю
    if pygame.sprite.spritecollide(copter, bounds, False):
        if copter.rect.top != -1: # упали на землю, взорвались и исчезли

            # выставляем месторасположение взрыва и добавляем его в список спрайтов для последующей отрисовки
            explosion.rect.bottom = copter.rect.bottom
            explosion.rect.left = copter.rect.left
            all_sprites.add(explosion)

            # убиваем наш веротлётик и отправляем его в стартовую позицию чтоб не мешался
            copter.kill()

    # После отрисовки всего, показываем экран
    pygame.display.flip()

pygame.quit()
