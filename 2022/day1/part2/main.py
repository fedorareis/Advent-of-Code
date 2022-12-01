with open('./input.txt') as f:
    curr = 0
    result = 0
    totals = []
    for line in f:
        if line == "\n":
            totals.append(curr)
            curr = 0
        else:
            curr += int(line)

    totals.sort(reverse=True)
    result = totals[0] + totals[1] + totals[2]
    print(result)
