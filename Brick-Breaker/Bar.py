
import pygame as py
from constants import * 

class Bar():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def draw(self, screen):
        py.draw.rect(screen, (0, 0, 250), (self.x, self.y, BAR_WIDTH, BAR_HEIGHT))
    
