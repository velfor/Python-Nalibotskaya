# подключаем модули
import pygame
import sys
# из модуля const берём всё
# ВНИМАНИЕ! НЕБЕЗОПАСНО! ТАК МОЖНО ИМПОРТИРОВАТЬ ТОЛЬКО СВОИ МОДУЛИ!

from const import *
from player import *
from meteor import *

#НАСТРОЙКА ИГРЫ (ИНИЦИАЛИЗАЦИЯ)
#инициализация библиотеки
pygame.init()
#создание экрана, указываем ширину и высоту в кортеже
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
# создаем часы для отслеживания FPS
clock = pygame.time.Clock()
#=====СОЗДАНИЕ ГРУПП=====
# создаем группу для всех спрайтов
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
#=====CОЗДАНИЕ ОБЪЕКТОВ=====
# создаем объект для игрока
player = Player()
# добавляем player в группу all_sprites
all_sprites.add(player)

for i in range(10):
    meteor = Meteor()
    all.sprites.add(meteor)
    meteors.add(meteor)



# переменная для управления циклом
run = True
# основной игровой цикл
while run:
    #0 задержка для фиксированного FPS
    clock.tick(FPS)
    #1 обработка событий
    for event in pygame.event.get():
        # если тип события - закрытие окна программы
        if event.type == pygame.QUIT:
            # выйти из программы
            run = False

    #2 действия и взаимодействия
    all_sprites.update()
    
    #3 отрисовка
    #заливаем экран черным цветом
    screen.fill(BLACK)
    # рисуем все спрайты (в памяти)
    all_sprites.draw(screen)
    # обновляем экран (выводим фон и спрайты на экран)
    pygame.display.update()

#здесь основной цикл игры закончился
# завершить pygame
pygame.quit()
# выйти
sys.exit()
