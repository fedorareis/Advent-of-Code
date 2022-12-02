with open('./input.txt') as f:
    result = 0
    decode = {
        'A': 1,
        'B': 2,
        'C': 3,
    }
    outcomePoints = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    for line in f:
        line = line.strip()
        parsed = line.split(' ')
        opp = decode[parsed[0]]
        outcome = parsed[1]
        result += outcomePoints[outcome]
        if outcome == 'Y':
            result += opp
        elif outcome == 'Z':
            result += (opp % 3) + 1
        else:
            result += opp - 1 if opp - 1 != 0 else 3

    print(result)
