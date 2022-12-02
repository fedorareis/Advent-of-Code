with open('./input.txt') as f:
    result = 0
    decode = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    for line in f:
        line = line.strip()
        parsed = line.split(' ')
        opp = decode[parsed[0]]
        me = decode[parsed[1]]
        result += me
        if opp == me:
            result += 3
        elif opp - me == -1 or opp - me == 2:
            result += 6

    print(result)
