import pygame as py
from constants import *
from Bar import Bar
from Ball import Ball
from game import InitBlocks, StartGame

def Main():
    
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    timer = py.time.Clock()
    level_num = 1
    bar = Bar(BAR_X, BAR_Y)
    ball_start_value = 1
    keep_going = True

    while keep_going:  
        blocks = InitBlocks(level_num)
        ball = Ball(BALL_START_X, BALL_START_Y, BALL_START_SPEED_X, BALL_START_SPEED_Y, ball_start_value)
        StartGame(screen, level_num, ball, bar, blocks, timer)

Main()