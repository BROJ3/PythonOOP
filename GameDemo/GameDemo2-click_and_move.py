import pygame
from pygame.locals import *
import sys
import random

#2 - define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

#initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()
ball_image = pygame.image.load('images/zuti.png')

#initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
ball_rect = pygame.Rect(ball_x,ball_y, BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)

#loop forever
while True:
    for event in pygame.event.get():
        #q for cosing
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #if user clicks
        if event.type ==pygame.MOUSEBUTTONUP:
            #if click is in the rect of the ball choose a new location
            if ball_rect.collidepoint(event.pos):
                ball_x = random.randrange(MAX_WIDTH)
                ball_y = random.randrange(MAX_HEIGHT)
                ball_rect = pygame.Rect(ball_x,ball_y,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)
                print(ball_rect)
                
    #do any "per frame actions"

    #clear the window
    window.fill(BLACK)

    #draw all winow elements
    #draw ball at the randomized locations
    window.blit(ball_image, (ball_x,ball_y))

    #update the window
    pygame.display.update()

    #set clock run
    clock.tick(FRAMES_PER_SECOND)

