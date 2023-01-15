import pygame
import sys
from config import *
from ball import Ball
 
# здесь определяются константы,
# классы и функции


def point_in_rect(pointx, pointy, rectx, recty, rect_width, rect_height):
    inx = rectx <= pointx <= rectx + rect_width
    iny = recty <= pointy <= recty + rect_height
    return inx and iny
    
 
# здесь происходит инициация,
# создание объектов

ball = Ball()
pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


#координаты ракетки
bat_x = BAT_OFFSET 
bat_y = (SCREEN_HEIGHT - BAT_HEIGHT) // 2
#скорость ракетки
bat_speed_y = 0

#score
f2 = pygame.font.SysFont('algerian', 48)

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
    ball.update()  

    #передвигаем ракетку по экрану
    
    keys = pygame.key.get_pressed()
    #если нажата
    if keys[pygame.K_s]:
        bat_speed_y = 10
    #если нажата
    if keys[pygame.K_w]:
        bat_speed_y = -10
    
    bat_y += bat_speed_y
    bat_speed_y = 0
    if bat_y <= 0:
        bat_y = 0
    elif bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
    
    #проверяем что мяч попал в ракетку
    #вычисляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx = ball.x - ball.r
    mid_lefty = ball.y
    
    mid_rightx = ball.x + ball.r
    mid_righty = ball.y
    
    mid_topx = ball.x
    mid_topy = ball.y - ball.r

    mid_bottomx = ball.x
    mid_bottomy = ball.y + ball.r
    
    #правая граница ракетки
    if point_in_rect(mid_leftx, mid_lefty, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_x = -ball.speed_x
        
    #верхняя граница ракетки
    if point_in_rect(mid_bottomx, mid_bottomy, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y
        
    #нижняя граница ракетки
    if point_in_rect(mid_topx, mid_topy, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y
    #score 
    score_left_text = f2.render(str(ball.left_score), True,
                  (255, 180, 0))
    
    # ОТРИСОВКА экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball.x, ball.y), ball.r)
    pygame.draw.rect(sc, ORANGE, (bat_x, bat_y, BAT_WIDTH, BAT_HEIGHT))
    #score
    sc.blit(score_left_text, (SCREEN_WIDTH//2 - 100, 10))
    pygame.display.update()





    
