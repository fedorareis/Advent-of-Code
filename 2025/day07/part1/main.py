with open("./input.txt") as f:
    result = 0
    ranges = []
    ranges_done = False
    for line in f:
        line = line.strip()
        if line == "":
            ranges_done = True
        elif not ranges_done:
            ranges.append([int(x) for x in line.split("-")])
        else:
            val = int(line)
            for range in ranges:
                if val >= range[0] and val <= range[1]:
                    result += 1
                    break

    print(result)
