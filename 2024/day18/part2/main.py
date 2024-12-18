import pprint

# size = 6
size = 70


def solveMaze(maze, x, y):
    visited = {"{},{}".format(x, y): True}
    queue = [(x, y, 0)]

    while len(queue) > 0:
        # print(queue)
        x, y, distance = queue.pop(0)
        if x == size and y == size:
            return distance

        if (
            x < size
            and maze[y][x + 1] != "#"
            and "{},{}".format(x + 1, y) not in visited
        ):
            visited["{},{}".format(x + 1, y)] = True
            queue.append((x + 1, y, distance + 1))

        if x > 0 and maze[y][x - 1] != "#" and "{},{}".format(x - 1, y) not in visited:
            visited["{},{}".format(x - 1, y)] = True
            queue.append((x - 1, y, distance + 1))

        if (
            y < size
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
    board = []
    moves = ""
    readingBoard = True

    for i in range((size + 1)):
        board.append(["."] * (size + 1))

    for line in f:
        input = line.strip()
        x, y = input.split(",")
        board[int(y)][int(x)] = "#"
        if solveMaze(board, 0, 0) == 0:
            result = input
            break

    # pprint.pprint(board)
    # result = solveMaze(board, 0, 0)

    print(result)
