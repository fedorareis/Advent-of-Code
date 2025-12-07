with open("./input.txt") as f:
    position = 50
    direction = ""
    clicks = ""
    result = 0
    for line in f:
        line = line.strip()
        direction = line[0]
        clicks = int(line[1:])
        result += int(clicks / 100)
        clicks = clicks % 100
        if direction == "R":
            position += clicks
            if position >= 100:
                position = position % 100
                result += 1
        elif direction == "L":
            position -= clicks % 100
            if position < 0:
                if clicks != abs(position):
                    result += 1
                position = 100 + position
            if position == 0:
                result += 1

    print(result)
