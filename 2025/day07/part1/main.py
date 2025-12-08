with open("./input.txt") as f:
    result = 0
    prev = ""
    for line in f:
        line = line.strip()
        if prev == "":
            prev = line
            continue

        line = list(line)
        for i in range(len(line)):
            if prev[i] == "S":
                line[i] = "|"

            if prev[i] == "|":
                if line[i] == "^":
                    line[i - 1] = "|"
                    line[i + 1] = "|"
                    result += 1
                else:
                    line[i] = "|"
        prev = "".join(line)

    print(result)
