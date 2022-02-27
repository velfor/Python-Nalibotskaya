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
# переменные для сторон
a = 10
b = 80
# переменные для левого верхнего угла прямоугольника
r_x = 20
r_y = SCREEN_HEIGHT // 2 - b//2
r_speedy = 10
#переменные для центра круга
c_x = SCREEN_WIDTH // 2
c_y = SCREEN_HEIGHT // 2
c_speed_y = 2
c_speed_x = 3
r = 10
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
        # если тип события - КЛАВИША НАЖАТА
##        if event.type == pygame.KEYDOWN:
##            #если нажата стрелка вниз
##            if event.key == pygame.K_DOWN:
##                #увеличиваем координату у прямоугольника
##                r_y += r_speedy
##            if event.key == pygame.K_UP:
##                r_y -= r_speedy
   
    #№ 2 - изменение состояния игровых объектов
    # =====КРУГ=====
    # изменение координат - движение по экрану
    c_x += c_speed_x
    c_y += c_speed_y

    # отталкивание от левой и правой границ
    if c_x + r > SCREEN_WIDTH or c_x - r < 0:
        c_speed_x = -c_speed_x
    # отталкивание от нижней и верхней границ
    if c_y + r > SCREEN_HEIGHT or c_y - r < 0:
        c_speed_y = -c_speed_y

    # =====ПРЯМОУГОЛЬНИК=====
    #управление с клавиатуры
    #получаем список (словарь) нажатых клавиш, у нажатых True
    keys = pygame.key.get_pressed()
    #если нажата стрелка вниз
    if keys[pygame.K_DOWN]:
        #увеличиваем координату у прямоугольника
        r_y += r_speedy
    if keys[pygame.K_UP]:
        r_y -= r_speedy
    if r_y < 0:
        r_y = 0
    if r_y + b > SCREEN_HEIGHT:
        r_y = SCREEN_HEIGHT - b
    
    # № 3 - перерисовка экрана
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (c_x, c_y), r)
    pygame.draw.rect(screen,WHITE,(r_x, r_y, a , b))
    pygame.display.flip()
    
        
    # задержка, чтобы скорость игры была постоянной на любых компах
    clock.tick(FPS)
