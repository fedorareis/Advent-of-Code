import re


def search(puzzle):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "X":
                # search for word
                return


with open("./ex.txt") as f:
    result = 0
    puzzle = []
    for line in f:
        val = line.strip()
        puzzle.append(list(val))

    search(puzzle)

    print(result)
