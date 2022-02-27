import pygame
import sys

# создание окна программы
pygame.display.set_mode((640,480))
# основной игровой цикл
while True:
    #обработка игровых событий
    for event in pygame.event.get():
        #если тип события - ВЫХОД
        if event.type == pygame.QUIT:
            #остановить модули библиотеки
            pygame.quit()
            #закрыть окно программы
            sys.exit()
