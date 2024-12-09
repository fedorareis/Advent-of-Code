with open("./input.txt") as f:
    result = 0
    for line in f:
        line = line.strip()
        increasing = None
        val = line.split(" ")

        for i in range(len(val) - 1):
            change = int(val[i]) - int(val[i + 1])
            if i == 0 and change > 0:
                increasing = True

            if change > 0 and change <= 3 and increasing:
                if i == len(val) - 2:
                    result += 1
                continue
            elif change < 0 and change >= -3 and not increasing:
                if i == len(val) - 2:
                    result += 1
                continue
            else:
                break

    print(result)
