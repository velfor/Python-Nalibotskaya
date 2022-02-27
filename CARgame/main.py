import pygame
import sys
from const import *
from obstacle import Obstacle
from car import Car
from bg import Background

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font('GorgeousPixel.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text_surface, text_rect)

def start_screen(screen):
    screen.fill(GREY)
    draw_text(screen, "Race", 48, YELLOW, SCREEN_WIDTH//2, 
        SCREEN_HEIGHT//4)
    draw_text(screen, "Left - left arrow, right - right arrow", 14, 
        YELLOW, SCREEN_WIDTH//2, 2*SCREEN_HEIGHT//4)
    draw_text(screen, "Press SPACE to play game", 20, 
        YELLOW, SCREEN_WIDTH//2, 3*SCREEN_HEIGHT//4)    
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            #если тип события - ВЫХОД
            if event.type == pygame.QUIT:
                #остановить модули библиотеки
                pygame.quit()
                #закрыть окно программы
                sys.exit()
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return;
                
#функция  - показ экрана "конец игры"
def game_over_screen(screen):
    screen.fill(GREY)
    draw_text(screen, "GAME OVER", 48, YELLOW, SCREEN_WIDTH//2, 
        SCREEN_HEIGHT//2)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            #если тип события - ВЫХОД
            if event.type == pygame.QUIT:
                #остановить модули библиотеки
                pygame.quit()
                #закрыть окно программы
                sys.exit()
#
pygame.init()                
# создание окна программы
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#создаем таймер для управления скоростью игры
clock = pygame.time.Clock()
# создаем игровые объекты
ob1 = Obstacle(0)#здесь вызовется init и объект создастся
ob2 = Obstacle(-240)
car = Car()
bg1 = Background(0)
bg2 = Background(-SCREEN_HEIGHT)
#создаём группу (список) со всеми игровыми объектами
all_sprites = pygame.sprite.Group()
#создаём группу (список) для препятствий
obstacles = pygame.sprite.Group()
#добавляем игровые объекты в группу
all_sprites.add(bg1)
all_sprites.add(bg2)
all_sprites.add(car)
all_sprites.add(ob1)
all_sprites.add(ob2)
obstacles.add(ob1)
obstacles.add(ob2)
#начальный экран
start_screen(screen)
# основной игровой цикл
while True:
    #№ 1 - обработка игровых событий (ввод пользователя)
    for event in pygame.event.get():
        #если тип события - ВЫХОД
        if event.type == pygame.QUIT:
            #остановить модули библиотеки
            pygame.quit()
            #закрыть окно программы
            sys.exit()
    #№ 2 - изменение состояния игровых объектов
    all_sprites.update()
    #проверка столкновений
    hits = pygame.sprite.spritecollide(car, obstacles, False)
    if hits:
        game_over_screen(screen)
    # № 3 - перерисовка экрана
    #screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.draw.rect(screen, BLACK, (0,0,SCREEN_WIDTH, 30))
    draw_text(screen, "Score: "+str(ob1.score + ob2.score), 24, YELLOW, 50, 14)
    pygame.display.flip()
    # задержка, чтобы скорость игры была постоянной на любых компах
    clock.tick(FPS)
