from const import *
import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ob.jpg").convert()
        self.image = pygame.transform.scale(self.image, (90,26))
        self.rect = self.image.get_rect()
        self.rect.left = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.bottom = y
        self.speedy = 3
        self.score = 0
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.left = randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.bottom = 0
            self.score += 1

    


        
