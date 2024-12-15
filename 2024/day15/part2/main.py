import pprint


def scoring(board):
    score = 0
    y = 0
    for row in board:
        x = 0
        for val in row:
            if val == "[":
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
            while board[y][tempX - 1] == "]" or board[y][tempX - 1] == "[":
                tempX = tempX - 1

            if board[y][tempX - 1] == "#":
                return

            if board[y][tempX - 1] == ".":
                while tempX <= x:
                    temp = board[y][tempX - 1]
                    board[y][tempX - 1] = board[y][tempX]
                    board[y][tempX] = temp
                    tempX += 1

            return
        case ">":
            if board[y][x + 1] == "#":
                return

            if board[y][x + 1] == ".":
                board[y][x + 1] = "@"
                board[y][x] = "."
                return

            tempX = x
            while board[y][tempX + 1] == "]" or board[y][tempX + 1] == "[":
                tempX = tempX + 1

            if board[y][tempX + 1] == "#":
                return

            if board[y][tempX + 1] == ".":
                while tempX >= x:
                    temp = board[y][tempX + 1]
                    board[y][tempX + 1] = board[y][tempX]
                    board[y][tempX] = temp
                    tempX = tempX - 1

            return
        case "^":
            if board[y - 1][x] == "#":
                return

            if board[y - 1][x] == ".":
                board[y - 1][x] = "@"
                board[y][x] = "."
                return

            tempY = y
            checkX = []
            row = 0
            if board[tempY - 1][x] == "[":
                checkX.append([x, x + 1])
            else:
                checkX.append([x, x - 1])
            tempY = tempY - 1
            while True:
                boxes = {}
                for tempX in checkX[row]:
                    if board[tempY - 1][tempX] == "#":
                        return
                    if board[tempY - 1][tempX] == "[":
                        boxes[tempX] = True
                        boxes[tempX + 1] = True
                    if board[tempY - 1][tempX] == "]":
                        boxes[tempX] = True
                        boxes[tempX - 1] = True
                if len(boxes.keys()) == 0:
                    break
                checkX.append(boxes.keys())
                tempY = tempY - 1
                row += 1

            while len(checkX) > 0:
                row = checkX.pop()
                for tempX in row:
                    temp = board[tempY - 1][tempX]
                    board[tempY - 1][tempX] = board[tempY][tempX]
                    board[tempY][tempX] = temp
                tempY += 1

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
            checkX = []
            row = 0
            if board[tempY + 1][x] == "[":
                checkX.append([x, x + 1])
            else:
                checkX.append([x, x - 1])
            tempY += 1
            while True:
                boxes = {}
                for tempX in checkX[row]:
                    if board[tempY + 1][tempX] == "#":
                        return
                    if board[tempY + 1][tempX] == "[":
                        boxes[tempX] = True
                        boxes[tempX + 1] = True
                    if board[tempY + 1][tempX] == "]":
                        boxes[tempX] = True
                        boxes[tempX - 1] = True
                if len(boxes.keys()) == 0:
                    break
                checkX.append(boxes.keys())
                tempY += 1
                row += 1

            while len(checkX) > 0:
                row = checkX.pop()
                for tempX in row:
                    temp = board[tempY + 1][tempX]
                    board[tempY + 1][tempX] = board[tempY][tempX]
                    board[tempY][tempX] = temp
                tempY = tempY - 1

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
