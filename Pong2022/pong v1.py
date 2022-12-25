import pygame
import sys
 
# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
BAT_WIDTH = 20
BAT_HEIGHT = 120
BAT_OFFSET = 10
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
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x = 5
ball_speed_y = 4

#координаты ракетки
bat_x = BAT_OFFSET 
bat_y = (SCREEN_HEIGHT - BAT_HEIGHT) // 2
#скорость ракетки
bat_speed_y = 0

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
    #верхний
    if ball_y <= r:
        ball_speed_y = -ball_speed_y
    #нижний
    if ball_y >= SCREEN_HEIGHT - r:
        ball_speed_y = -ball_speed_y    

    #передвигаем ракетку по экрану
    
    bat_y += bat_speed_y
    
    keys = pygame.key.get_pressed()
    #если нажата
    if keys[pygame.K_s]:
        bat_speed_y = 10
    #если нажата
    if keys[pygame.K_w]:
        bat_speed_y = -10
        
    if bat_y <= 0:
        
        bat_y = 0
        
    elif bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
        
    # обновление экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc, ORANGE, (bat_x, bat_y, BAT_WIDTH, BAT_HEIGHT))
    pygame.display.update()





    
