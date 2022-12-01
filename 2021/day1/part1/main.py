with open('./input.txt') as f:
    prev = None
    count = 0
    for line in f:
        curr = int(line)
        if prev is None:
            prev = curr
        if curr > prev:
            count += 1
        prev = curr

    print(count)
