with open("./input.txt") as f:
    result = 0
    input = []
    fs = []

    for line in f:
        val = line.strip()
        input = list(val)

    id = 0
    for index, value in enumerate(input):
        value = int(value)
        if index % 2 == 0:
            while value > 0:
                fs.append(id)
                value = value - 1
            id += 1
        else:
            while value > 0:
                fs.append(".")
                value = value - 1

    start = 0
    end = len(fs) - 1
    while end > start:
        # print(fs)
        temp = ""
        if fs[end] != ".":
            temp = fs[end]
            while fs[start] != "." and start != len(fs) - 1:
                start += 1
            if start >= end:
                break
            fs[start] = temp
            fs[end] = "."
        else:
            end = end - 1

    # print(fs)
    for idx, val in enumerate(fs):
        # print(str(idx) + "," + str(val))
        if val == ".":
            continue

        temp = idx * int(val)
        # print(temp)
        result += temp

    print(result)
