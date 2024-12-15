import pprint


def scoring(board):
    score = 0
    y = 0
    for row in board:
        x = 0
        for val in row:
            if val == "O":
                score += (100 * y) + x
            x += 1
        y += 1

    return score


def findBot(board):
    y = 0
    for row in board:
        x = 0
        for val in row:
            if val == "@":
                return x, y
            x += 1
        y += 1


def move(board, dir):
    x, y = findBot(board)
    match dir:
        case "<":
            if board[y][x - 1] == "#":
                return

            if board[y][x - 1] == ".":
                board[y][x - 1] = "@"
                board[y][x] = "."
                return

            tempX = x
            while board[y][tempX - 1] == "O":
                tempX = tempX - 1

            if board[y][tempX - 1] == "#":
                return

            if board[y][tempX - 1] == ".":
                board[y][tempX - 1] = "O"
                board[y][x - 1] = "@"
                board[y][x] = "."

            return
        case ">":
            if board[y][x + 1] == "#":
                return

            if board[y][x + 1] == ".":
                board[y][x + 1] = "@"
                board[y][x] = "."
                return

            tempX = x
            while board[y][tempX + 1] == "O":
                tempX = tempX + 1

            if board[y][tempX + 1] == "#":
                return

            if board[y][tempX + 1] == ".":
                board[y][tempX + 1] = "O"
                board[y][x + 1] = "@"
                board[y][x] = "."

            return
        case "^":
            if board[y - 1][x] == "#":
                return

            if board[y - 1][x] == ".":
                board[y - 1][x] = "@"
                board[y][x] = "."
                return

            tempY = y
            while board[tempY - 1][x] == "O":
                tempY = tempY - 1

            if board[tempY - 1][x] == "#":
                return

            if board[tempY - 1][x] == ".":
                board[tempY - 1][x] = "O"
                board[y - 1][x] = "@"
                board[y][x] = "."

            return
        case "v":
            if board[y + 1][x] == "#":
                return

            if board[y + 1][x] == ".":
                board[y + 1][x] = "@"
                board[y][x] = "."
                return

            tempY = y
            while board[tempY + 1][x] == "O":
                tempY = tempY + 1

            if board[tempY + 1][x] == "#":
                return

            if board[tempY + 1][x] == ".":
                board[tempY + 1][x] = "O"
                board[y + 1][x] = "@"
                board[y][x] = "."

            return


with open("./input.txt") as f:
    result = 0
    board = []
    moves = ""
    readingBoard = True

    for line in f:
        input = line.strip()
        if input == "":
            readingBoard = False
        elif readingBoard:
            board.append(list(input))
        else:
            moves = moves + input

    for dir in moves:
        move(board, dir)

    result = scoring(board)

    print(result)
