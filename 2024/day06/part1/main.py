import pprint


def search(puzzle, x, y, dir):
    spaces = 0
    # pprint.pprint(puzzle)

    match dir:
        case "up":
            while y >= 0:
                if puzzle[y][x] != "X":
                    spaces += 1
                puzzle[y][x] = "X"
                if y == 0:
                    return spaces
                elif puzzle[y - 1][x] == "#":
                    return spaces + search(puzzle, x, y, "right")
                else:
                    y = y - 1
        case "right":
            while x < len(puzzle[y]):
                if puzzle[y][x] != "X":
                    spaces += 1
                puzzle[y][x] = "X"
                if x == len(puzzle[y]) - 1:
                    return spaces
                elif puzzle[y][x + 1] == "#":
                    return spaces + search(puzzle, x, y, "down")
                else:
                    x = x + 1
        case "down":
            while y < len(puzzle):
                if puzzle[y][x] != "X":
                    spaces += 1
                puzzle[y][x] = "X"
                if y == len(puzzle) - 1:
                    return spaces
                elif puzzle[y + 1][x] == "#":
                    return spaces + search(puzzle, x, y, "left")
                else:
                    y = y + 1
        case "left":
            while x >= 0:
                if puzzle[y][x] != "X":
                    spaces += 1
                puzzle[y][x] = "X"
                if x == 0:
                    return spaces
                elif puzzle[y][x - 1] == "#":
                    return spaces + search(puzzle, x, y, "up")
                else:
                    x = x - 1


with open("./input.txt") as f:
    result = 0
    puzzle = []
    startX = 0
    startY = 0
    row = 0
    for line in f:
        val = line.strip()
        puzzle.append(list(val))

        temp = line.find("^")
        if temp != -1:
            startX = temp
            startY = row

        row += 1

    result = search(puzzle, startX, startY, "up")

    print(result)
