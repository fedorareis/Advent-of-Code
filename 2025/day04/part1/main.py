with open("./input.txt") as f:
    result = 0
    map = []
    for line in f:
        line = line.strip()
        map.append(list(line))

    rows = len(map)
    cols = len(map[0])
    for y in range(rows):
        for x in range(cols):
            rolls = 0
            if map[y][x] == "@":
                if x > 0 and map[y][x - 1] == "@":
                    rolls += 1
                if y > 0 and map[y - 1][x] == "@":
                    rolls += 1
                if y > 0 and x > 0 and map[y - 1][x - 1] == "@":
                    rolls += 1
                if x < cols - 1 and map[y][x + 1] == "@":
                    rolls += 1
                if y < rows - 1 and map[y + 1][x] == "@":
                    rolls += 1
                if y < rows - 1 and x < cols - 1 and map[y + 1][x + 1] == "@":
                    rolls += 1
                if y < rows - 1 and x > 0 and map[y + 1][x - 1] == "@":
                    rolls += 1
                if y > 0 and x < cols - 1 and map[y - 1][x + 1] == "@":
                    rolls += 1
                if rolls < 4:
                    result += 1

    print(result)
