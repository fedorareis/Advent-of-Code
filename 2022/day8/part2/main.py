def scenic(forest, row, col):
    isVisible = True
    height = int(forest[row][col])
    left = 0
    right = 0
    up = 0
    down = 0
    decX = col - 1
    incX = col + 1
    decY = row - 1
    incY = row + 1

    while decX >= 0 and isVisible:
        left += 1
        if height <= int(forest[row][decX]):
            isVisible = False
        decX += -1
    if left == 0:
        return left

    isVisible = True
    while incX <= len(forest) - 1 and isVisible:
        right += 1
        if height <= int(forest[row][incX]):
            isVisible = False
        incX += 1
    if right == 0:
        return right

    isVisible = True
    while decY >= 0 and isVisible:
        down += 1
        if height <= int(forest[decY][col]):
            isVisible = False
        decY += -1
    if down == 0:
        return down

    isVisible = True
    while incY <= len(forest) - 1 and isVisible:
        up += 1
        if height <= int(forest[incY][col]):
            isVisible = False
        incY += 1

    return up * down * left * right


with open('./input.txt') as f:
    result = 0
    forest = []
    for line in f:
        line = line.strip()
        forest.append(list(line))

    y = 0
    for row in forest:
        x = 0
        for col in row:
            score = scenic(forest, y, x)
            if score > result:
                result = score
            x += 1
        y += 1

    print(result)
