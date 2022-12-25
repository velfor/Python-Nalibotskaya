import pygame
import sys
 
# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# радиус мяча
r = 20
# координаты мяча
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x = 3
ball_speed_y = 1
 
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
    # передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # Выход за края экрана
    # левый
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x = -ball_speed_x
    # правый
    if ball_x >= SCREEN_WIDTH - r:
        # летел направо - полетел налево
        ball_speed_x = -ball_speed_x
        
    # обновление экрана
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.display.update()





    
