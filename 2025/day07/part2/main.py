with open("./input.txt") as f:
    result = 0
    ranges = []
    for line in f:
        line = line.strip()
        if line == "":
            for val in ranges:
                result += val[1] - val[0] + 1
            break
        else:
            temp = [int(x) for x in line.split("-")]
            end = False
            count = 0
            while not end:
                expand = False
                for i in range(len(ranges)):
                    val = ranges[i]
                    # equal
                    if temp[0] >= val[0] and temp[1] <= val[1]:
                        temp = ranges.pop(i)
                        break
                    # replace
                    if temp[0] <= val[0] and temp[1] >= val[1]:
                        expand = True
                        val[0] = temp[0]
                        val[1] = temp[1]
                        temp = ranges.pop(i)
                        break
                    # exapnd upper bound
                    if temp[0] >= val[0] and temp[0] <= val[1]:
                        expand = True
                        if temp[1] > val[1]:
                            val[1] = temp[1]
                        temp = ranges.pop(i)
                        break
                    # expand lower bound
                    if temp[1] >= val[0] and temp[1] <= val[1]:
                        expand = True
                        if temp[0] < val[0]:
                            val[0] = temp[0]
                        temp = ranges.pop(i)
                        break
                if not expand:
                    ranges.append(temp)
                    end = True

    print(result)
