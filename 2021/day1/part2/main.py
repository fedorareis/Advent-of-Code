with open('./input.txt') as f:
    prev = None
    count = 0
    input = []
    for line in f:
        input.append(int(line))
    for idx, val in enumerate(input):
        curr = input[idx] + input[idx+1] + input[idx+2]
        if prev is None:
            prev = curr
        if curr > prev:
            count += 1
        prev = curr
        if idx+3 == len(input):
            break

    print(count)
