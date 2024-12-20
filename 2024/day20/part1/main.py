import pprint


def findStart(maze):
    y = 0
    for row in maze:
        x = 0
        for val in row:
            if val == "S":
                return x, y
            x += 1
        y += 1


def solveMaze(maze, x, y):
    visited = {"{},{}".format(x, y): True}
    queue = [(x, y, 0)]
    shortest = len(maze[0]) * len(maze)

    while len(queue) > 0:
        # print(queue)
        x, y, distance = queue.pop(0)
        # print("visiting", y, x)
        if maze[y][x] == "E" and distance < shortest:
            return distance

        if (
            x < len(maze[y])
            and maze[y][x + 1] != "#"
            and "{},{}".format(x + 1, y) not in visited
        ):
            visited["{},{}".format(x + 1, y)] = True
            queue.append((x + 1, y, distance + 1))

        if x > 0 and maze[y][x - 1] != "#" and "{},{}".format(x - 1, y) not in visited:
            visited["{},{}".format(x - 1, y)] = True
            queue.append((x - 1, y, distance + 1))

        if (
            y < len(maze)
            and maze[y + 1][x] != "#"
            and "{},{}".format(x, y + 1) not in visited
        ):
            visited["{},{}".format(x, y + 1)] = True
            queue.append((x, y + 1, distance + 1))

        if y > 0 and maze[y - 1][x] != "#" and "{},{}".format(x, y - 1) not in visited:
            visited["{},{}".format(x, y - 1)] = True
            queue.append((x, y - 1, distance + 1))

    return 0


with open("./input.txt") as f:
    result = 0
    maze = []

    for line in f:
        input = line.strip()
        maze.append(list(input))

    startX, startY = findStart(maze)

    longestRoute = solveMaze(maze, startX, startY)
    temp = {}
    print("longest", longestRoute)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (
                y > 0
                and y < len(maze) - 1
                and maze[y][x] == "#"
                and maze[y - 1][x] != "#"
                and maze[y + 1][x] != "#"
            ):
                maze[y][x] = "."
                route = solveMaze(maze, startX, startY)
                # print(x, y, route)
                maze[y][x] = "#"
                # if longestRoute - route in temp:
                #     temp[longestRoute - route] = temp[longestRoute - route] + 1
                # else:
                #     temp[longestRoute - route] = 1
                if longestRoute - route >= 100:
                    result += 1
            elif (
                x > 0
                and x < len(maze[y]) - 1
                and maze[y][x] == "#"
                and maze[y][x - 1] != "#"
                and maze[y][x + 1] != "#"
            ):
                maze[y][x] = "."
                # pprint.pprint(maze)
                route = solveMaze(maze, startX, startY)
                # print(x, y, route)
                maze[y][x] = "#"
                # if longestRoute - route in temp:
                #     temp[longestRoute - route] = temp[longestRoute - route] + 1
                # else:
                #     temp[longestRoute - route] = 1
                if longestRoute - route >= 100:
                    result += 1

    # pprint.pprint(maze)
    # print(temp)
    print(result)
