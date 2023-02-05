from config import *
import pygame

class Brick:
    def __init__(self, posX, posY, color):
        self.x = posX
        self.y = posY
        self.color = color
    
    def update(self):
        pass