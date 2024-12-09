with open("./input.txt") as f:
    first = []
    second = {}
    result = 0
    for line in f:
        val = line.split("   ")
        first.append(int(val[0]))
        tmp = int(val[1])
        if tmp in second:
            second[tmp] = second[tmp] + 1
        else:
            second[tmp] = 1

    for val in first:
        if val in second:
            result += val * second[val]

    print(result)
