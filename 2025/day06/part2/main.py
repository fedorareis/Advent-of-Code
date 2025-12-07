def toColumns(input, operators):
    output = []
    temps = []

    for i in range(len(operators)):
        temp = ""
        for j in range(len(input)):
            temp += input[j][i]
        temps.append(temp)

        if temp.strip() == "" or i == len(operators) - 1:
            newlist = []
            # print(temps)
            for num in temps:
                temp = num.strip()
                if temp != "":
                    newlist.append(int(temp))
            output.append(newlist)
            temps = []

    return output


with open("./input.txt") as f:
    result = 0
    problems = []
    lines = []
    for line in f:
        temp = line.strip().split()
        if temp[0] != "+" and temp[0] != "*":
            lines.append(line)
        else:
            problems = toColumns(lines, line)
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
