#1 - imports
import pygame
from pygame.locals import *
import sys
import random

#2 - define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 680
FPS=30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

#3 - init the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock  = pygame.time.Clock()

# loading asets
ball_image = pygame.image.load('../images/ooooo/grb.png')

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

ball_X = random.randrange(MAX_HEIGHT)
ball_Y = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_PER_FRAME
y_speed = N_PIXELS_PER_FRAME

#6 loop forever
while True:
    for event in pygame.event.get():
        #cose if x'ing out
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #if touching corner, switch direction in X
    if (ball_X<0) or (ball_X>=MAX_WIDTH):
        x_speed=-x_speed 

        #if touching corner, switch direction in X
    if (ball_Y<0) or (ball_Y>=MAX_HEIGHT):
        y_speed=-y_speed 

    ball_X = ball_X + x_speed
    ball_Y = ball_Y + y_speed

    window.fill(BLACK)

    window.blit(ball_image,(ball_X,ball_Y))

    pygame.display.update()

    clock.tick(FPS)