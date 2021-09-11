import copy

# maze = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
#         [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]]
# length = len(maze)

# visitedmaze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

paths = []


def ratinmaze(maze, start, end, path, visitedm, length,destination_X,destination_Y):

    if (start > - 1 and end > -1) and (start < length and end < length):
        if maze[start][end] == 1 and visitedm[start][end] == 0:
            if start == destination_X and end == destination_Y:
                visitedm[start][end] = path
                paths.append(visitedm)
            visitedm[start][end] = path
            path += 1
            ratinmaze(maze, start, end + 1, path, copy.deepcopy(visitedm),length,destination_X,destination_Y), ratinmaze(maze, start - 1, end, path,
                                                                                      copy.deepcopy(
                                                                                          visitedm),length,destination_X,destination_Y), ratinmaze(maze,
                                                                                                                start,
                                                                                                                end - 1,
                                                                                                                path,
                                                                                                                copy.deepcopy(
                                                                                                                    visitedm),length,destination_X,destination_Y), ratinmaze(
                maze, start + 1, end, path, copy.deepcopy(visitedm),length,destination_X,destination_Y)
# ratinmaze(maze,0,0,1,visitedmaze)
