import pygame as py
from constants import * 

class Ball():
    def __init__(self, x, y, speed_x, speed_y, value):
        super().__init__()
        
        self.x = x 
        self.y = y 
        self.value = value
        self.speed_x = speed_x
        self.speed_y = speed_y


    def draw(self, screen):
        
        py.draw.circle(screen, WHITE, (self.x, self.y), BALL_SIZE)

    def move(self, vel):
        self.x += self.speed_x * vel
        self.y += self.speed_y * vel

    def increment(self):
        self.value += 1

    
    