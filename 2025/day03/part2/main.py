with open("./input.txt") as f:
    result = 0
    for line in f:
        joltage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        line = line.strip()
        for i in range(0, len(line)):
            val = int(line[i])
            set = False
            for j in range(0, len(joltage)):
                # print(i, j, val, joltage[j], joltage, len(line) - j - 1)
                if set:
                    joltage[j] = 0
                    continue
                if val > joltage[j] and i <= (len(line) - 1) - (len(joltage) - j - 1):
                    joltage[j] = val
                    set = True
        # print(line + " : " + "".join([str(x) for x in joltage]))
        result += int("".join([str(x) for x in joltage]))

    print(result)
