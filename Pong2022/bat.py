from config import *
import pygame

class Bat:
    def __init__(self):
        #координаты ракетки
        self.x = BAT_OFFSET 
        self.y = (SCREEN_HEIGHT - BAT_HEIGHT) // 2
        #скорость ракетки
        self.speed_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        #если нажата
        if keys[pygame.K_s]:
            self.speed_y = 10
        #если нажата
        if keys[pygame.K_w]:
            self.speed_y = -10
        self.y += self.speed_y
        self.speed_y = 0
        if self.y <= 0:
            self.y = 0
        elif self.y >= SCREEN_HEIGHT - BAT_HEIGHT:
            self.y = SCREEN_HEIGHT - BAT_HEIGHT
