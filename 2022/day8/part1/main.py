def visible(forest, row, col):
    isVisible = True
    height = int(forest[row][col])
    decX = col - 1
    incX = col + 1
    decY = row - 1
    incY = row + 1

    while decX >= 0 and isVisible:
        if height <= int(forest[row][decX]):
            isVisible = False
        decX += -1
    if isVisible:
        return isVisible

    isVisible = True
    while incX <= len(forest) - 1 and isVisible:
        if height <= int(forest[row][incX]):
            isVisible = False
        incX += 1
    if isVisible:
        return isVisible

    isVisible = True
    while decY >= 0 and isVisible:
        if height <= int(forest[decY][col]):
            isVisible = False
        decY += -1
    if isVisible:
        return isVisible

    isVisible = True
    while incY <= len(forest) - 1 and isVisible:
        if height <= int(forest[incY][col]):
            isVisible = False
        incY += 1

    return isVisible


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
            isVisible = visible(forest, y, x)
            # print(str(y) + ',' + str(x) + ': ' + str(isVisible))
            if isVisible:
                result += 1
            x += 1
        y += 1

    print(result)
