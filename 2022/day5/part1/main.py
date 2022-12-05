with open('./input.txt') as f:
    stacks = {
        "1": ["R", "G", "H", "Q", "S", "B", "T", "N"],
        "2": ["H", "S", "F", "D", "P", "Z", "J"],
        "3": ["Z", "H", "V"],
        "4": ["M", "Z", "J", "F", "G", "H"],
        "5": ["T", "Z", "C", "D", "L", "M", "S", "R"],
        "6": ["M", "T", "W", "V", "H", "Z", "J"],
        "7": ["T", "F", "P", "L", "Z"],
        "8": ["Q", "V", "W", "S"],
        "9": ["W", "H", "L", "M", "T", "D", "N", "C"],
    }
    # stacks = {
    #     "1": ["Z", "N"],
    #     "2": ["M", "C", "D"],
    #     "3": ["P"],
    # }
    result = ""
    for line in f:
        line = line.strip()
        input = line.split("move ")
        input = input[1].split(" from ")
        amount = int(input[0])
        input = input[1].split(" to ")
        start = input[0]
        end = input[1]
        while amount > 0:
            stacks[end].append(stacks[start].pop())
            amount -= 1

    for key, value in stacks.items():
        result += value.pop()
    print(result)
