with open("./ex.txt") as f:
    first = []
    second = []
    result = 0
    for line in f:
        val = line.split("   ")
        first.append(int(val[0]))
        second.append(int(val[1]))

    first.sort()
    second.sort()

    for i in range(len(first)):
        temp = first[i] - second[i]
        if temp < 0:
            temp = temp * -1
        result += temp

    print(result)
