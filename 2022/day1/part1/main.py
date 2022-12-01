with open('./input.txt') as f:
    curr = 0
    result = 0
    for line in f:
        if line == "\n":
            if curr > result:
                result = curr
            curr = 0
        else:
            curr += int(line)

    print(result)
