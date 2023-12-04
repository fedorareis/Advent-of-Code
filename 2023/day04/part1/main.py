with open('./input.txt') as f:
    result = 0

    for line in f:
        line = line.strip()
        score = 0
        first = True
        temp = line.split(": ")
        temp = temp[1].split(" | ")
        winning = {}
        for val in temp[0].split(" "):
            if val != "":
                winning[val] = True
        
        for val in temp[1].split(" "):
            if val != "" and val in winning:
                if first:
                    score = 1
                    first = False
                else:
                    score = score * 2

        result += score

    print(result)
