with open('./input.txt') as f:
    result = 0

    for line in f:
        line = line.strip()
        temp = [int(x) for x in line.split(" ")]
        for val in temp:
            result += val

    print(result)
