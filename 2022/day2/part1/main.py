# hints:
#   "The first column is what your opponent is going to play:
#    A for Rock, B for Paper, and C for Scissors. The second column--"
# ---
#   The second column, you reason, must be what you should play in response:
#      X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious,
#      so the responses must have been carefully chosen.
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
        # my initial attempt is more readable but I decided to be clever and see if I could use math for determining the win conditions
        # instead of directly have checks for the rock, paper, scissors win conditions
        elif opp - me == -1 or opp - me == 2:
            result += 6

    print(result)
