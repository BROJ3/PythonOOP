#import packages
import pygame
from pygame.locals import *
import sys 
import random

#2 - define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

BALL_WIDTH_HEIGHT=100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# 3 - initialize the world
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load Assets
ball_image = pygame.image.load('images/zuti.png')
target_image = pygame.image.load('images/lopta.png')

# 5 - initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
target_rect = pygame.Rect(TARGET_X,TARGET_Y,TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT)

# 6 - loop forever
while True:

    # 7 - check for handle events
    for event in pygame.event.get():
        #close if x-d out
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        #see if user pressed a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x = ball_x - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ball_x = ball_x + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ball_y = ball_y - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ball_y = ball_y + N_PIXELS_TO_MOVE

    # 8 - Do any "per frame" actions
    ball_Rect = pygame.Rect(ball_x,ball_y,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)

    if ball_Rect.colliderect(target_rect):
        print("Ball is touhcing the target")
    else:
        print("NOT touching")

    # 9 - clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(target_image,(TARGET_X,TARGET_Y)) #draw the target

    window.blit(ball_image, (ball_x,ball_y)) # draw the ball

    # 11 - update the window
    pygame.display.update()

    #slo things down a bit
    clock.tick(FRAMES_PER_SECOND)