from const import *
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, starty):
        pygame.sprite.Sprite.__init__(self)
        background = pygame.image.load('road.jpg').convert()
        self.image = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = starty
        self.speedy = 3
        
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.bottom = 0