from const import *
import pygame

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,80))
        # убираем черный цвет фона
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 10

    def update(self):
        keys = pygame.key.get_pressed()
        #если нажата стрелка вниз
        if keys[pygame.K_LEFT]:
        #изменяем координату x прямоугольника
            self.rect.x -= self.speedx
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        #если вышел за границу экрана, то возврат на эту границу
        #левая граница
        if self.rect.left <= 0:
            self.rect.left = 0
        #правая граница
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    #def draw(self,screen):
    #    pygame.draw.rect(screen,BLACK,(self.rect.x, self.rect.y, self.rect.width , self.height))
    
