import pygame
import sys
from config import *
from ball import Ball
from bat import Bat
from brick import Brick
from brickRow import BrickRow
 
def point_in_rect(pointx, pointy, rectx, recty, rect_width, rect_height):
    inx = rectx <= pointx <= (rectx + rect_width)
    iny = recty <= pointy <= (recty + rect_height)
    return inx and iny

def check_collisions(ball, bat):
    pass

def ball_hit_bricks(ball, brick_row):
    mid_leftx = ball.x - ball.r
    mid_lefty = ball.y
    mid_rightx = ball.x + ball.r
    mid_righty = ball.y
    mid_topx = ball.x
    mid_topy = ball.y - ball.r
    mid_bottomx = ball.x
    mid_bottomy = ball.y + ball.r
    for brick in brick_row.row:
        if point_in_rect(mid_topx, mid_topy, brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT):
            brick_row.row.remove(brick)
            ball.speed_y = -ball.speed_y
            break

pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# здесь происходит инициация,
# создание объектов
ball = Ball()
bat = Bat()
brick_row = BrickRow()
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
    bat.update()

    
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
    if point_in_rect(mid_leftx, mid_lefty, bat.x, bat.y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_x = -ball.speed_x
        
    for brick in brick_row.row:
        if point_in_rect(mid_topx, mid_topy, brick.x,
            brick.y, BRICK_WIDTH, BRICK_HEIGHT):
            ball.speed_y = -ball.speed_y
            #и всё остальное
        
    #верхняя граница ракетки
    if point_in_rect(mid_bottomx, mid_bottomy, bat.x, bat.y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y
        
    #нижняя граница ракетки
    if point_in_rect(mid_topx, mid_topy, bat.x, bat.y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y
    #score 
    score_left_text = f2.render(str(ball.left_score), True,
                  (255, 180, 0))
    #ПРОВЕРКА СТОЛКНОВЕНИЙ МЯЧА С КИРПИЧАМИ
    ball_hit_bricks(ball, brick_row)
    
    # ОТРИСОВКА экрана
    sc.fill(BLACK)
    pygame.draw.circle(sc, ORANGE,(ball.x, ball.y), ball.r)
    pygame.draw.rect(sc, ORANGE, (bat.x, bat.y, BAT_WIDTH, BAT_HEIGHT))
    for brick in brick_row.row:
        pygame.draw.rect(sc, BLACK, (brick.x, brick.y, 
            BRICK_WIDTH, BRICK_HEIGHT), 1)
        pygame.draw.rect(sc, brick.color, (brick.x+1, brick.y+1, 
            BRICK_WIDTH-1, BRICK_HEIGHT-1))
    #score
    sc.blit(score_left_text, (SCREEN_WIDTH//2 - 100, 10))
    pygame.display.update()





    
