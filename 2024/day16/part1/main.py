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
    queue = [(x, y, 0, "East", 0)]
    routes = []

    while len(queue) > 0:
        print(queue)
        x, y, distance, dir, score = queue.pop(0)
        if maze[y][x] == "E":
            routes.append(score)
            continue

        if maze[y][x + 1] != "#" and "{},{}".format(x + 1, y) not in visited:
            if dir != "East":
                score += 1001
            else:
                score += 1

            if maze[y][x + 1] != "E":
                visited["{},{}".format(x + 1, y)] = True
            queue.append((x + 1, y, distance + 1, "East", score))

        if maze[y][x - 1] != "#" and "{},{}".format(x - 1, y) not in visited:
            if dir != "West":
                score += 1001
            else:
                score += 1

            if maze[y][x - 1] != "E":
                visited["{},{}".format(x - 1, y)] = True
            queue.append((x - 1, y, distance + 1, "West", score))

        if maze[y + 1][x] != "#" and "{},{}".format(x, y + 1) not in visited:
            if dir != "South":
                score += 1001
            else:
                score += 1

            if maze[y + 1][x] != "E":
                visited["{},{}".format(x, y + 1)] = True
            queue.append((x, y + 1, distance + 1, "South", score))

        if maze[y - 1][x] != "#" and "{},{}".format(x, y - 1) not in visited:
            if dir != "North":
                score += 1001
            else:
                score += 1

            if maze[y - 1][x] != "E":
                visited["{},{}".format(x, y - 1)] = True
            queue.append((x, y - 1, distance + 1, "North", score))

    return routes


with open("./ex.txt") as f:
    result = 0
    maze = []

    for line in f:
        input = line.strip()
        maze.append(list(input))

    x, y = findStart(maze)

    routes = solveMaze(maze, x, y)

    print(routes)
    result = routes.pop(0)
    for val in routes:
        if val < result:
            result = val

    print(result)
