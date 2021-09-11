import os
import pygame
import RATINMAZE
import math
import time
import copy
import pprint
pygame.init()

length = 10
visited_maze = [[0 for j in range(length)] for i in range(length)]

# maze = copy.deepcopy(visited_maze)
maze = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

# length = 10
displaysize = length * 50

title = pygame.display.set_caption("RAT_IN_A_MAZE")
# rat_img = pygame.image.load('C:/Users/moham/Downloads/rat.png')
# wall_img = pygame.image.load('C:/Users/moham/Downloads/wall (2).png')
#             # (54, 139, 133)
#             # (255, 77, 0)
start_x = 0
start_y = 0
destination_X = 9
destination_Y = 0
def grid_coloring(length,color,color2,color3,screen):
    # pygame.display.update()
    for i in range(length):
        for j in range(length):
            if maze[i][j] == 0:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color, ((50 * j) + 1, (50 * i), 48, 48))
            elif i == destination_X and j == destination_Y:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color3, ((50 * j) + 1, (50 * i), 48, 48))
            else:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color2, ((50 * j) + 1, (50 * i), 48, 48))
            pygame.display.update()



    # while True:
        # pygame.display.update()
        # pygame.mouse.get_cursor()

            # print('das')
                        # pygame.display.update()
                    # if event.type == pygame.KEYDOWN:
                        # print(x,y)





    # for i in range(length):
    #     for j in range(length):
    #         if maze[i][j] == 0:
    #             pygame.draw.rect(screen, color, ((50 * j) + 1, (50 * i), 48, 48))
    #         elif i == destination_X and j == destination_Y:
    #             pygame.draw.rect(screen, color3, ((50 * j) + 1, (50 * i), 48, 48))
    #         else:
    #             pygame.draw.rect(screen, color2, ((50 * j) + 1, (50 * i), 48, 48))
def shortest(screen):
    shortest_path = length**2
    for paths in RATINMAZE.paths:
        pathlist = [i for path in paths for i in path]
        if max(pathlist) < shortest_path:
            (shortest_list := paths)
            shortest_path = max(pathlist)
    print_logic(shortest_path, shortest_list, screen)
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RIGHT:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
def longest(screen):
    longest = 0
    for paths in RATINMAZE.paths:
        pathlist = [i for path in paths for i in path]
        if max(pathlist) > longest:
            longest = max(pathlist)
            (longest_list := paths)
    print_logic(longest,longest_list,screen)
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RIGHT:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()



def full_path(screen):
    print('path',len(RATINMAZE.paths))
    k = 0
    for paths in RATINMAZE.paths:

        pprint.pprint(RATINMAZE.paths)
        pathlist = [i for path in paths for i in path]
        max_val = max(pathlist)
        print(pathlist)
        pygame.display.update()
        grid_coloring(length, (0, 0, 0), (255, 255, 255),(255, 0, 0), screen)
        # pygame.display.update()
        print_logic(max_val,paths,screen)
        pygame.display.update()
        run = True
        while run:

            for keyboard in pygame.event.get():

                if keyboard.type == pygame.KEYDOWN:
                    if keyboard.key == pygame.K_ESCAPE:
                        print(k, "kkkk")
                        k = 1
                        run = False
                    if keyboard.key == pygame.K_RIGHT or keyboard.key == pygame.K_SPACE:

                        run = False

                if keyboard.type == pygame.QUIT:
                    pygame.quit()


        if k == 1:
            print("Fs")
            break

def print_logic(max_val,paths,screen):
    for element in range(1, max_val + 1):
        for row in range(len(paths)):
            if element in paths[row]:
                pos = paths[row].index(element)
                # print(pos,row)
                step = pygame.font.Font("/home/hafsal/Downloads/Roboto/Roboto-Thin.ttf", 40)
                title_rendered = step.render(f"{element}", True, (255, 255, 255))
                if row == destination_X and pos == destination_Y:
                    pygame.draw.rect(screen, (255, 0, 0), ((50 * pos) + 1, (50 * row), 48, 48))
                    screen.blit(title_rendered, ((50 * pos) + 1,(50 * row)))
                else:
                    pygame.draw.rect(screen, (54, 139, 133), ((50 * pos) + 1, (50 * row), 48, 48))
                    screen.blit(title_rendered, ((50 * pos) + 1, (50 * row)))
def mazeboard_display():
    screen = pygame.display.set_mode((displaysize, displaysize))
    return screen


def mazeboard(setting_type):
    screen = mazeboard_display()
    screen.fill((178, 190, 181))
    grid_coloring(length, (0, 0, 0), (255, 255, 255), (255, 0, 0), screen)
    pygame.display.update()
    RATINMAZE.ratinmaze(maze, start_x, start_y, 1, visited_maze,length,destination_X,destination_Y)
    print("FDSfdsdsf")

    # pprint.pprint(longest())
    print("DSFdsffsd")
    total_paths = len(RATINMAZE.paths)
    print(total_paths)
    print(setting_type)
    if setting_type == 1:
        full_path(screen)
    elif setting_type == 2:
        longest(screen)
    else:
        shortest(screen)
    pygame.display.update()
    grid_coloring(length, (0, 0, 0), (255, 255, 255),(255, 0, 0),screen)

    # run = True
    # while run:
    #     print("entered")
    #     for event in pygame.event.get():
    #
    #         if event.type == pygame.K_ESCAPE:
    #             run = False
    #         if event.type == pygame.QUIT:
    #             pygame.quit()



#
def mainfun():
    mainscreen = pygame.display.set_mode((500, 500))

    title_font = pygame.font.Font("/home/hafsal/Downloads/Roboto/Roboto-Thin.ttf", 40)
    title_rendered = title_font.render("Rat In A Maze", True, (0, 0, 0))




    roboto_font = pygame.font.Font('/home/hafsal/Downloads/Roboto/Roboto-Thin.ttf', 30)
    roboto_rendered = roboto_font.render("start", True, (0, 0, 0))



    short_font = pygame.font.Font('/home/hafsal/Downloads/Roboto/Roboto-Thin.ttf', 30)
    short_rendered = short_font.render("Short path", True, (0, 0, 0))


    normal_font = pygame.font.Font('/home/hafsal/Downloads/Roboto/Roboto-Thin.ttf', 30)
    normal_rendered =normal_font.render("Normal", True, (0, 0, 0))

    long_font = pygame.font.Font('/home/hafsal/Downloads/Roboto/Roboto-Thin.ttf', 30)
    long_rendered = long_font.render("Long path", True, (0, 0, 0))

    img = pygame.image.load('/home/hafsal/Downloads/gear.png')

    setting_type = 1

    run = True
    while run:

        mainscreen.fill((84, 110, 122))
        pygame.draw.rect(mainscreen, (200, 200, 200), (0, 30, 500, 50))


        short_path = pygame.draw.rect(mainscreen, (200, 200, 200), (0, 100, 150, 40))
        start_button = pygame.draw.rect(mainscreen, (200, 200, 200), (180, 210, 150, 40))
        normal_button = pygame.draw.rect(mainscreen, (200,200,200), (180, 100, 150, 40))

        long_button = pygame.draw.rect(mainscreen, (200, 200, 200), (360, 100, 150, 40))
        mainscreen.blit(title_rendered, (131.5, 33))
        mainscreen.blit(roboto_rendered, (225, 210))
        mainscreen.blit(short_rendered, (10, 100))
        mainscreen.blit(normal_rendered, (205, 100))

        mainscreen.blit(long_rendered, (365, 100))
        mainscreen.blit(img, (450, 450))
        if setting_type == 1:
            normal_rendered = normal_font.render("Normal", True, (255,255,255))
        else:
            normal_rendered = normal_font.render("Normal", True, (0,0,0))
        if setting_type == 2:
            long_rendered = long_font.render("Long path", True, (255,255,255))
        else:
            long_rendered = long_font.render("Long path", True, (0,0,0))
        if setting_type == 3:
            short_rendered = short_font.render("Short path", True, (255,255,255))
        else:
            short_rendered = short_font.render("Short path", True, (0,0,0))
        x, y = pygame.mouse.get_pos()
        # print(x, y)
        #

        pygame.display.update()
        for event in pygame.event.get():

            if start_button.collidepoint(x,y) :
                roboto_rendered = roboto_font.render("start", True, (221,44,0))
            else:
                roboto_rendered = roboto_font.render("start", True, (0,0 ,0))
            # # else:
            # #     long_rendered = long_font.render("Long path", True, (0,0,0))
            # if normal_button.collidepoint(x,y):
            #
            #     normal_rendered = normal_font.render("Normal", True,(221,44,0))
            #     # normal_button = pygame.draw.rect(mainscreen,(0,0,0) , (180, 100, 150, 40))
            #     # pygame.display.update()
            # # else:
            # #     normal_rendered = normal_font.render("Normal", True, (0,0,0))
            #     # normal_button = pygame.draw.rect(mainscreen, (0,0,0), (180, 100, 150, 40))
            # if short_path.collidepoint(x,y) :
            #     short_rendered = short_font.render("Short path", True,(221,44,0))
            #     # short_path = pygame.draw.rect(mainscreen, (255,255,255), (0, 100, 150, 40),5)
            #     # pygame.display.update()
            #
            #     # short_path = pygame.draw.rect(mainscreen, (200, 200, 200), (0, 100, 150, 40),0)
            # # pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_button.collidepoint(x,y):
                    setting_type = 1

                if long_button.collidepoint(x,y):
                    setting_type = 2
                    print(setting_type)
                if short_path.collidepoint(x,y):
                    setting_type = 3
                if start_button.collidepoint(x,y):
                    print(x,y)
                    print(setting_type)
                    mazeboard(setting_type)

                if x in range(450,485) and y in range(450,485):
                    settings_screen = mazeboard_display()
                    settings_screen.fill((178, 190, 181))

                    # pygame.display.flip()
                    # print(pygame.display.Info())
                    running = True
                    while running:

                        grid_coloring(length, (0, 0, 0), (255, 255, 255), (255, 0, 0),
                                      settings_screen)

                        # print(maze)
                        x, y = pygame.mouse.get_pos()
                        # for event in pygame.event.get():
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                            if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_ESCAPE:
                                    running = False
                                if event.key == pygame.K_a:
                                    global maze
                                    maze = [[0 for _ in range(length)] for _ in range(length)]
                                for i in range(length):
                                    for j in range(length):

                                        if globals()[f"rect{i}{j}"].collidepoint(x, y):
                                            global destination_Y, destination_X
                                            old_x,old_y = destination_X,destination_Y
                                            if event.key == pygame.K_r:
                                                print("Df")


                                                destination_X,destination_Y = i,j
                                                maze[destination_X][destination_Y] = 1
                                                maze[old_x][old_y] = 0
                                            if event.key == pygame.K_w:
                                                maze[i][j] = 1
                                                print('ds')
                                            if event.key == pygame.K_b:
                                                maze[i][j] = 0
                                                print("DS")



                                            print("FDSfd",destination_X,destination_Y)
                                            pprint.pprint(maze)
                                            pygame.display.update()
                                            # pygame.display.flip()/
                        # pygame.display.update()
                        # print(destination_X,destination_Y)
                    pygame.display.update()
                    # x, y = pygame.mouse.get_pos()
                    # print(x, y)
                    # print(rect1.x,rect1.y)



                # input()
            if event.type == pygame.QUIT:
                run = False

    # mazeboard()

if  __name__ == '__main__':

    mainfun()

