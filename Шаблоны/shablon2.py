import pygame
import sys

FPS = 60

# создание окна программы
pygame.display.set_mode((640,480))
#создаем таймер для управдения скоростью игры
clock = pygame.time.Clock()

# основной игровой цикл
while True:
    # задержка, чтобы скорость игры была постоянной на любых компах
    clock.tick(FPS)
    
    #№ 1 - обработка игровых событий
    for event in pygame.event.get():
        #если тип события - ВЫХОД
        if event.type == pygame.QUIT:
            #остановить модули библиотеки
            pygame.quit()
            #закрыть окно программы
            sys.exit()

    #№ 2 - изменение состояния игровых объектов

    # № 3 - перерисовка экрана
    pygame.display.flip()
