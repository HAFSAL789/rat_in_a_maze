import copy

# storing all possible paths
paths = []


def ratinmaze(maze, start, end, path, visitedm, length, destination_X, destination_Y):
    if (start > - 1 and end > -1) and (start < length and end < length):
        # if it is a not visited step
        if maze[start][end] == 1 and visitedm[start][end] == 0:
            # if it is the destination
            if start == destination_X and end == destination_Y:
                # set step in visited
                visitedm[start][end] = path
                # append the new path
                paths.append(visitedm)
            # set visited
            visitedm[start][end] = path

            # increase path step
            path += 1

            # for left,right,up,down steps
            ratinmaze(maze, start, end + 1, path, copy.deepcopy(visitedm), length, destination_X, destination_Y), \
            ratinmaze(maze, start - 1, end, path, copy.deepcopy(visitedm), length, destination_X, destination_Y), \
            ratinmaze(maze, start, end - 1, path, copy.deepcopy(visitedm), length, destination_X, destination_Y), \
            ratinmaze(maze, start + 1, end, path, copy.deepcopy(visitedm), length, destination_X, destination_Y)
