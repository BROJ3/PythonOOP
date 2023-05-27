#1-Import packages
import pygame
from pygame.locals import *
import sys

#2- define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 - load assets(images, sounds etc.)

#5 initialize variables

#loop forever
while True:
    #7 - check for and handle events
    for event in pygame.event.get():
        print(event)
        print(event.type, event.dict)
        if event.type == 771:
            print(event.dict['text'])
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    window.fill(BLACK)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)