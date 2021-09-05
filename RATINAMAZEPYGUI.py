import os
import pygame
import RATINMAZE
import math
import time

pygame.init()
length = RATINMAZE.length
# length = 10
displaysize = length*50
screen = pygame.display.set_mode((displaysize,displaysize))
# rat_img = pygame.image.load('C:/Users/moham/Downloads/rat.png')
# wall_img = pygame.image.load('C:/Users/moham/Downloads/wall (2).png')
def mainfun():
    screen.fill((178, 190, 181))
    RATINMAZE.ratinmaze(RATINMAZE.maze, 0, 0, 1, RATINMAZE.visitedmaze)
    for i in range(length):
        for j in range(length):
            if RATINMAZE.maze[i][j] == 0:
    #             # (54, 139, 133)
    #             # (255, 77, 0)
                pygame.draw.rect(screen, (0,0, 0), ((50 * j) + 1, (50 * i), 48, 48))
            else:
                pygame.draw.rect(screen, (255,255,255), ((50 * j) + 1, (50 * i), 48, 48))

    for paths in RATINMAZE.paths:
        pathlist = []
        for path in paths:
            pathlist.extend(path)
        print(pathlist)
        for i in range(1,max(pathlist)+1):
            pos = pathlist.index(i)
            pos_x = pos//length
            if pos_x > 1:
                poss = pos - (length*pos_x)
                print(poss)
            else:
                print(pos)
            # if pos_x == math.floor(pos_x):
            #
            # print(pos_x)
            # pygame.draw.a
            # pygame.draw.line(screen,(i*))
            # screen.blit(rat_img, (pos*10, pos*10))
            # pygame.draw.rect(screen, (0,255,0), ((50 * pos-1), (50 * pos-1), 48, 48))
        pygame.display.update()
            # print(pathlist)
        # input("wanna continue")
        # for step in pathlist:
        #     pathlist.index()
        #
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # rat = rat_img.

mainfun()


