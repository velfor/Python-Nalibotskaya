import pygame
import sys
#константы
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# создание окна программы
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#создаем таймер для управления скоростью игры
clock = pygame.time.Clock()

# создаем игровые объекты
# переменные для левого верхнего угла
x = 20
y = 20
# переменные для сторон
a = 80
b = 60
speedx = 3
#переменные для центра круга
c_x = 50
c_y = 50
c_speed_y = 2

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
    if x + a > SCREEN_WIDTH or x < 0:
        speedx = -speedx 
    
    x += speedx

    if c_y + 40 > SCREEN_HEIGHT or c_y - 40 < 0:
        c_speed_y = -c_speed_y
        
    c_y += c_speed_y
    
    # № 3 - перерисовка экрана
    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE, (x,y,a,b))
    pygame.draw.circle(screen, YELLOW, (c_x, c_y), 40)
    pygame.display.flip()
    
        
    # задержка, чтобы скорость игры была постоянной на любых компах
    clock.tick(FPS)
