#!/usr/bin/env python2

import pygame
import random
import sys
from cass import  Main


WIDTH = 750
HEIGHT = 500
FPS = 30
keys=[False, False, False, False]
move = 8
plawidth = 166
plaheight = 74

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAM")
clock = pygame.time.Clock()     ## For syncing the FPS

## set image
PLAi = pygame.image.load("./asset/main.jpeg")
bg = pygame.image.load("./asset/BG.png")


## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
PLAyer = Main(RED, plawidth, plaheight)
PLAyer.rect.x == 10
all_sprites.add(PLAyer)

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_LEFT:
                keys[1]=True
            elif event.key==pygame.K_DOWN:
                keys[2]=True
            elif event.key==pygame.K_RIGHT:
                keys[3]=True
        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False


    #2 Update
    all_sprites.update()

    """
                PLAyer.moveLeft(5)
                PLAyer.moveRight(5)
    """


    #3 Draw/render
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))

    

    all_sprites.draw(screen)
    ########################

    ### Your code comes here

    ########################

    if keys [0]:
        if PLAyer.rect.y > 0:
            PLAyer.moveUp(move)
    elif keys [2]:
        if PLAyer.rect.y < HEIGHT - plaheight:
            PLAyer.moveDown(move)
    if keys [1]:
        if PLAyer.rect.x > 0:
            PLAyer.moveLeft(move)
    elif keys [3]:
        if PLAyer.rect.x < WIDTH - plawidth:
            PLAyer.moveRight(move)

    ## Done after drawing everything to the screen
    pygame.display.flip()

    
pygame.quit()
sys.exit()
