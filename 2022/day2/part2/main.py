# hints:
#   "The first column is what your opponent is going to play:
#    A for Rock, B for Paper, and C for Scissors. The second column--"
# ---
#   The second column, you learn, is the outcome of the round:
#      X for Lose, Y for Draw, and Z for Win.
#
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
#    (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
#    (0 if you lost, 3 if the round was a draw, and 6 if you won).

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
            # since this is a draw we can just use the value of the opponents selection
            result += opp
        elif outcome == 'Z':
            # When you win the item you used is the next on the list, but you need to wrap around
            # for rock to beat scissors. Each subsequent item on the list is 1 more than the value
            # of the previous one. So if we mod the value first that solves our wrap around problem
            # and then we can just add 1 to that.
            result += (opp % 3) + 1
        else:
            # Similar to winning we have a wrap around problem. This time in the other direction
            # I'm probably being too clever here and should have stuck with my previous amath answer
            # where I just subtract 1 and use a ternary so if that equals 0 it returns 3 instead
            # but I really wanted to see if I could find a relatively simple equation that works
            result += ((opp + 1) % 3) + 1

    print(result)
