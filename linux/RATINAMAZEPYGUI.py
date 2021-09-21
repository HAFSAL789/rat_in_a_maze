import pygame
import RATINMAZE
import os


# to color grids
def grid_coloring(length, color, color2, color3, color4, screen):
    for i in range(length):
        for j in range(length):
            # black for blocks
            if maze[i][j] == 0:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color, ((50 * j) + 1, (50 * i), 48, 48))
            # blue for starting point
            elif i == start_x and j == start_y:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color4, ((50 * j) + 1, (50 * i), 48, 48))
            # red for destination
            elif i == destination_X and j == destination_Y:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color3, ((50 * j) + 1, (50 * i), 48, 48))
            # white for paths
            else:
                globals()[f"rect{i}{j}"] = pygame.draw.rect(screen, color2, ((50 * j) + 1, (50 * i), 48, 48))
            pygame.display.update()


# to find shortest path
def shortest(screen):
    # set a max
    shortest_path = length ** 2

    # to find the shortest path
    for paths in RATINMAZE.paths:
        pathlist = [i for path in paths for i in path]
        if max(pathlist) < shortest_path:
            (shortest_list := paths)
            shortest_path = max(pathlist)

    # to print the shortest path
    print_logic(shortest_path, shortest_list, screen)

    # press escape space right to perform actions
    escape_space_right_quit()


# press escape space right to perform actions
def escape_space_right_quit():
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RIGHT:
                    run = False
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


# to find longest path
def longest(screen):
    longest = 0

    # longest path
    for paths in RATINMAZE.paths:
        pathlist = [i for path in paths for i in path]
        if max(pathlist) > longest:
            longest = max(pathlist)
            (longest_list := paths)

    # print the path
    print_logic(longest, longest_list, screen)
    escape_space_right_quit()


# to find the full paths
def full_path(screen):
    running = False

    # loop through each path
    for paths in RATINMAZE.paths:
        pathlist = [i for path in paths for i in path]
        max_val = max(pathlist)

        # to color over previously printed path
        grid_coloring(length, (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255), screen)

        # to print path
        print_logic(max_val, paths, screen)
        pygame.display.update()

        # press escape space right to perform actions
        run = True
        while run:
            for keyboard in pygame.event.get():
                if keyboard.type == pygame.KEYDOWN:
                    # to perform escape op
                    if keyboard.key == pygame.K_ESCAPE:
                        running = True
                        run = False
                    # to perform space or right_key op
                    if keyboard.key == pygame.K_RIGHT or keyboard.key == pygame.K_SPACE:
                        run = False
                # to quit
                if keyboard.type == pygame.QUIT:
                    pygame.quit()
                    run = False

        if running:
            break


# to print a path
def print_logic(max_val, paths, screen):
    for element in range(1, max_val + 1):
        for row in range(len(paths)):
            if element in paths[row]:
                pos = paths[row].index(element)
                step = pygame.font.Font(os.getcwd() + "/Roboto/Roboto-Thin.ttf", 40)
                title_rendered = step.render(f"{element}", True, (255, 255, 255))
                # to print in red
                if row == destination_X and pos == destination_Y:
                    pygame.draw.rect(screen, (255, 0, 0), ((50 * pos) + 1, (50 * row), 48, 48))
                    screen.blit(title_rendered, ((50 * pos) + 1, (50 * row)))
                # to print in blue
                elif row == start_x and pos == start_y:
                    pygame.draw.rect(screen, (0, 0, 255), ((50 * pos) + 1, (50 * row), 48, 48))
                    screen.blit(title_rendered, ((50 * pos) + 1, (50 * row)))
                # to print in (54, 139, 133)
                else:
                    pygame.draw.rect(screen, (54, 139, 133), ((50 * pos) + 1, (50 * row), 48, 48))
                    screen.blit(title_rendered, ((50 * pos) + 1, (50 * row)))


# displaying on board
def mazeboard_display():
    screen = pygame.display.set_mode((displaysize, displaysize))
    return screen


# mazeboard fun
def mazeboard(setting_type, maze):
    global visited_maze
    screen = mazeboard_display()
    screen.fill((178, 190, 181))
    grid_coloring(length, (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255), screen)
    # pygame.display.update()

    # reset paths to null list on clicking start
    RATINMAZE.paths = []

    # calling ratinmaze algo
    RATINMAZE.ratinmaze(maze, start_x, start_y, 1, visited_maze, length, destination_X, destination_Y)

    # reset visited_maze into 0
    visited_maze = [[0 for _ in range(length)] for _ in range(length)]

    # choosing full,long,short path
    if setting_type == 1:
        full_path(screen)
    elif setting_type == 2:
        longest(screen)
    else:
        shortest(screen)

    # pygame.display.update()
    # grid_coloring(length, (0, 0, 0), (255, 255, 255),(255, 0, 0),screen)


def font_thin(name, size, color):
    font_thin = pygame.font.Font(os.getcwd() + "/Roboto/Roboto-Thin.ttf", size)
    return font_thin.render(name, True, color)


def mainfun():
    global maze

    mainscreen = pygame.display.set_mode((500, 500))

    title_rendered = font_thin("Rat In A Maze", 40, (0, 0, 0))

    roboto_rendered = font_thin("start", 30, (0, 0, 0))

    short_rendered = font_thin("Short path", 30, (0, 0, 0))

    normal_rendered = font_thin("Normal", 30, (0, 0, 0))

    long_rendered = font_thin("Long path", 30, (0, 0, 0))
    # ----------------------------------------------------------------------------------------------
    img = pygame.image.load(os.getcwd() + "/Roboto/gear.png")

    # default settings into normal path
    setting_type = 1

    run = True
    while run:

        mainscreen.fill((84, 110, 122))

        # draw rect's on main screen
        pygame.draw.rect(mainscreen, (200, 200, 200), (0, 30, 500, 50))
        short_path = pygame.draw.rect(mainscreen, (200, 200, 200), (0, 100, 150, 40))
        start_button = pygame.draw.rect(mainscreen, (200, 200, 200), (180, 210, 150, 40))
        normal_button = pygame.draw.rect(mainscreen, (200, 200, 200), (180, 100, 150, 40))
        long_button = pygame.draw.rect(mainscreen, (200, 200, 200), (360, 100, 150, 40))

        # blit
        mainscreen.blit(title_rendered, (131.5, 33))
        mainscreen.blit(roboto_rendered, (225, 210))
        mainscreen.blit(short_rendered, (10, 100))
        mainscreen.blit(normal_rendered, (205, 100))
        mainscreen.blit(long_rendered, (365, 100))
        mainscreen.blit(img, (450, 450))

        # changing color for setting button
        if setting_type == 1:
            normal_rendered = font_thin("Normal", 30, (255, 255, 255))
        else:
            normal_rendered = font_thin("Normal", 30, (0, 0, 0))
        if setting_type == 2:
            long_rendered = font_thin("Long path", 30, (255, 255, 255))
        else:
            long_rendered = font_thin("Long path", 30, (0, 0, 0))
        if setting_type == 3:
            short_rendered = font_thin("Short path", 30, (255, 255, 255))
        else:
            short_rendered = font_thin("Short path", 30, (0, 0, 0))

        # get mouse pos
        x, y = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            # change color for start button
            if start_button.collidepoint(x, y):
                roboto_rendered = font_thin("start", 30, (221, 44, 0))
            else:
                roboto_rendered = font_thin("start", 30, (0, 0, 0))

            # choosing settings normal / long/ short
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_button.collidepoint(x, y):
                    setting_type = 1
                if long_button.collidepoint(x, y):
                    setting_type = 2
                if short_path.collidepoint(x, y):
                    setting_type = 3
                # start the game
                if start_button.collidepoint(x, y):
                    mazeboard(setting_type, maze)

                # if clicked on gear icon
                if x in range(450, 485) and y in range(450, 485):
                    # setting screen
                    settings_screen = mazeboard_display()
                    settings_screen.fill((178, 190, 181))

                    running = True
                    while running:
                        # color settings grid
                        grid_coloring(length, (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255),
                                      settings_screen)
                        x, y = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    running = False
                                # set display all grid into black
                                if event.key == pygame.K_a:
                                    maze = [[0 for _ in range(length)] for _ in range(length)]

                                for i in range(length):
                                    for j in range(length):
                                        # to customize grid
                                        if globals()[f"rect{i}{j}"].collidepoint(x, y):
                                            # r for red
                                            if event.key == pygame.K_r:
                                                global destination_Y, destination_X
                                                old_x, old_y = destination_X, destination_Y
                                                destination_X, destination_Y = i, j
                                                maze[destination_X][destination_Y] = 1
                                                maze[old_x][old_y] = 0
                                            # s for blue
                                            if event.key == pygame.K_s:
                                                global start_x, start_y
                                                old_start_x, old_start_y = start_x, start_y
                                                start_x, start_y = i, j
                                                maze[start_x][start_y] = 1
                                                maze[old_start_x][old_start_y] = 0
                                            # w for white
                                            if event.key == pygame.K_w:
                                                maze[i][j] = 1
                                            # b for black
                                            if event.key == pygame.K_b:
                                                maze[i][j] = 0

                                            pygame.display.update()

                    pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


if __name__ == '__main__':
    pygame.init()

    # length of the board
    length = 10
    # visitedmaze with all values 0
    visited_maze = [[0 for _ in range(length)] for _ in range(length)]

    # maze
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
    # global maze
    displaysize = length * 50

    title = pygame.display.set_caption("RAT_IN_A_MAZE")

    # starting points
    start_x = 0
    start_y = 0

    # destination points
    destination_X = 9
    destination_Y = 0

    mainfun()
