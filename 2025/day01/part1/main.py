with open("./input.txt") as f:
    position = 50
    direction = ""
    clicks = ""
    result = 0
    for line in f:
        line = line.strip()
        direction = line[0]
        clicks = int(line[1:])
        if direction == "R":
            position += clicks
            position = position % 100
        elif direction == "L":
            position -= clicks % 100
            if position < 0:
                position = 100 + position
        if position == 0:
            result += 1

    print(result)
