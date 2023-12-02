with open('./ex.txt') as f:
    result = 0
    for line in f:

        for idx, val in enumerate(line):
            result += val

    print(result)
