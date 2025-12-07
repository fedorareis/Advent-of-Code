with open("./input.txt") as f:
    result = 0
    for line in f:
        first = 0
        second = 0
        line = line.strip()
        for i in range(0, len(line)):
            val = int(line[i])
            if val > first and i != len(line) - 1:
                first = val
                second = 0
            elif val > second:
                second = val
        result += int(str(first) + str(second))

    print(result)
