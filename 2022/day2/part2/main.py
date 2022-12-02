with open('./input.txt') as f:
    result = 0
    decode = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
    }
    value = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3,
    }
    outcomePoints = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    win = {
        'Rock': 'Paper',
        'Paper': 'Scissors',
        'Scissors': 'Rock',
    }
    lose = {
        'Paper': 'Rock',
        'Scissors': 'Paper',
        'Rock': 'Scissors',
    }
    for line in f:
        line = line.strip()
        parsed = line.split(' ')
        opp = decode[parsed[0]]
        outcome = parsed[1]
        result += outcomePoints[outcome]
        if outcome == 'Y':
            result += value[opp]
        elif outcome == 'Z':
            result += value[win[opp]]
        else:
            result += value[lose[opp]]

    print(result)
