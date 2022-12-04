import pygame
import random
from heli import Copter, enemyCopter, Bullet
from explosions import *
from settings import *
from pathlib import Path


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("helicopter fly")
clock = pygame.time.Clock()
my_font = pygame.font.SysFont(None, 20)

background = pygame.image.load( Path(__file__).parent / "img" / "bckgnd" / bckgnd )#.convert()
background_rect = background.get_rect()

explosion = Explosion()
copter = Copter(heli_pic) # наш вертолет
bounds = pygame.sprite.Group()
bounds.add( [Bound(HEIGHT-1), Bound(0)] )# граница по земле и по небу
all_sprites, enemyCopters, bullets = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
all_sprites.add(copter)

# Цикл игры
running = 1
while running:
    running += 1

    text_surface = my_font.render(f'Здоровье : {copter.health} Патроны : {copter.ammo} Сбито {copter.killed_enemies} вертолетов', False, (0, 0, 0))

    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # раз в 200 циклов прилетает вражеский вертолетик
    if not (running % 200):
        enemy = enemyCopter("helicopter_1.png", copter)
        enemyCopters.add(enemy)
        all_sprites.add(enemy)

    # считываем нажатия на клавиши
    keystate = pygame.key.get_pressed()
    # Пробелом стреляем раз в 10 тиков и если остались патроны
    if keystate[pygame.K_SPACE]:
        if not (running % 10) and copter.ammo:
            bullet = Bullet(copter.rect.right, copter.rect.centery, 1)
            all_sprites.add(bullet)
            bullets.add(bullet)
            copter.ammo -= 1

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = 0

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE):
                pass

        # ЛКМ - перезапуск игры
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #  левая кнопка мыши
                running = 1
                copter = Copter(heli_pic) # наш вертолет
                all_sprites.empty()
                enemyCopters.empty()
                bullets.empty()
                all_sprites.add(copter)

    # Обновление координат всех объектов из all_sprites
    all_sprites.update()

    # врезающиеся друг в друга вертолеты    
    heli_crash = pygame.sprite.spritecollide(copter, enemyCopters, True)
    if heli_crash:
        explosion.rect.center = copter.rect.center
        all_sprites.add(explosion)
        copter.kill()

    # попадания пулек во врага
    enemy_hits = pygame.sprite.groupcollide(bullets, enemyCopters, True, True)
    if enemy_hits:
        blt = list( enemy_hits.keys() )[0]
        explosion.rect.center = blt.rect.center
        all_sprites.add(explosion)
        copter.killed_enemies += 1

    # Проверка, врезания в землю
    if pygame.sprite.spritecollide(copter, bounds, False):
        if copter.rect.top != -1: # упали на землю, взорвались и исчезли

            # выставляем месторасположение взрыва и добавляем его в список спрайтов для последующей отрисовки
            explosion.rect.center = copter.rect.center
            all_sprites.add(explosion)

            # убиваем наш веротлётик
            copter.kill()

    # Рендеринг
    screen.blit(background, background_rect)
    screen.blit(text_surface, (10, 10))
    all_sprites.draw(screen)

    # После отрисовки всего, показываем экран
    pygame.display.flip()

pygame.quit()
