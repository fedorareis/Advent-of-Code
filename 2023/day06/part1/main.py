with open('./input.txt') as f:
    result = 0

    for line in f:
        line = line.strip()
        for val in line:
            result += val

    print(result)
