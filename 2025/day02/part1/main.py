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
                temp = str(i)
                if temp[int(len(temp) / 2) :] == temp[: int(len(temp) / 2)]:
                    result += i

    print(result)
