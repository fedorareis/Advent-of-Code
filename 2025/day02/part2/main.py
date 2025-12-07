import re

with open("./input.txt") as f:
    result = 0
    for line in f:
        line = line.strip()
        ranges = line.split(",")
        for r in ranges:
            bounds = r.split("-")
            start = int(bounds[0])
            end = int(bounds[1])
            for i in range(start, end + 1):
                val = str(i)
                for j in range(1, int(len(val) / 2) + 1):
                    sub = val[:j]
                    positions = [match.start() for match in re.finditer(sub, val)]
                    if len(positions) * j == len(val) and len(positions) > 1:
                        # print(sub + " in " + val)
                        result += i
                        break

    print(result)
