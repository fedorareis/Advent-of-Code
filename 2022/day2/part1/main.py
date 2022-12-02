with open('./input.txt') as f:
    result = 0
    decode = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors',
    }
    value = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3,
    }
    isWin = {
        'C X': True,
        'A Y': True,
        'B Z': True,
    }
    for line in f:
        line = line.strip()
        parsed = line.split(' ')
        opp = decode[parsed[0]]
        me = decode[parsed[1]]
        result += value[me]
        if opp == me:
            result += 3
        elif line in isWin:
            result += 6

    print(result)
