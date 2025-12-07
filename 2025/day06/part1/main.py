with open("./input.txt") as f:
    result = 0
    problems = []
    for line in f:
        line = line.strip()
        temp = line.split()
        if temp[0] != "+" and temp[0] != "*":
            if len(problems) == 0:
                for val in temp:
                    problems.append([int(val)])
            else:
                for i in range(len(temp)):
                    problems[i].append(int(temp[i]))
        else:
            for i in range(len(temp)):
                if temp[i] == "*":
                    val = 1
                    for x in problems[i]:
                        val *= x
                    result += val
                if temp[i] == "+":
                    for x in problems[i]:
                        result += x

    print(result)
