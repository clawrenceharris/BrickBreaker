import pygame as py
from constants import *

class Block():
    
    def __init__(self, x, y, value, width, height, is_ball_block):
        super().__init__()
        self.value = value
        self.x = x * UNIT_SIZE + 2 
        self.y = y * UNIT_SIZE + 52
        self.width = width
        self.height = height
        self.is_ball_block = is_ball_block


    def draw(self, screen):
        color = ()
        if not self.is_ball_block:
            font = py.font.Font('freesansbold.ttf', 15)
            text = font.render(str(self.value), True, WHITE)
            
            if not self.value * 10 >= 240:
                color = (self.value * 10, 40 ,150)
            else:
                color = (240, 40 ,150)
            py.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
            
                
            screen.blit(text, (self.x + (self.width / 2) - text.get_rect().width / 2, self.y + (self.height / 2) - text.get_rect().height / 2))
        else:
            font = py.font.Font('freesansbold.ttf', 15)
            text = font.render("+ ", True, WHITE)

            py.draw.rect(screen, (249, 233, 110), (self.x, self.y, self.width, self.height))
            py.draw.circle(screen, WHITE, ((self.x + self.width / 2) + 10 , self.y + self.height / 2), BALL_SIZE)
            screen.blit(text, (self.x + (self.width / 2) - text.get_rect().width / 2, self.y + (self.height / 2) - text.get_rect().height / 2))


    def decrement(self, value):
        if self.value > 0:
            self.value -= value

    def moveDown(self):
        self.y += UNIT_SIZE
    