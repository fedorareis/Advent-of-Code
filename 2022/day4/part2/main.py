with open('./input.txt') as f:
    result = 0
    for line in f:
        line = line.strip()
        pairs = line.split(",")
        first = pairs[0].split("-")
        second = pairs[1].split("-")
        if (int(first[0]) <= int(second[0]) and int(second[0]) <= int(first[1])) or (int(second[0]) <= int(first[0]) and int(first[0]) <= int(second[1])):
            result += 1
    print(result)
