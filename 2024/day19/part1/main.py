import pprint
import itertools


def canMatch(pattern, towels):
    possible = itertools.combinations_with_replacement(towels, len(pattern))
    print(pattern, list(possible))

    for temp in possible:
        if temp == pattern:
            return True

    # for towel in towels:
    #     if towel == pattern[: len(towel)]:
    #         possible.append(towel)

    # print(pattern)
    # while len(possible) > 0:
    #     newPossible = []
    #     for curr in possible:
    #         for towel in towels:
    #             temp = curr + towel
    #             if temp == pattern[: len(temp)]:
    #                 newPossible.append(temp)
    #                 if len(temp) == len(pattern):
    #                     return True
    #     possible = newPossible

    # print(pattern, possible)
    return False


def canMatch2(pattern, towelMap):
    possible = []

    if pattern[0] not in towelMap:
        return False

    for towel in towelMap[pattern[0]]:
        if towel == pattern[: len(towel)]:
            possible.append(towel)

    # print(pattern)
    while len(possible) > 0:
        newPossible = []
        for curr in possible:
            if len(curr) < len(pattern):
                if pattern[len(curr)] not in towelMap:
                    return False
                for towel in towelMap[pattern[len(curr)]]:
                    temp = curr + towel
                    if len(temp) <= len(pattern) and temp == pattern[: len(temp)]:
                        newPossible.append(temp)
                        if len(temp) == len(pattern):
                            return True
        possible = newPossible

    # print(pattern, possible)
    return False


def generateMap(towels):
    lookup = {}
    for towel in towels:
        if towel[0] in lookup:
            lookup[towel[0]].append(towel)
        else:
            lookup[towel[0]] = [towel]

    return lookup


def generatePossibilities(towels, length):
    allPossible = {}
    prev = towels
    underLength = True

    while underLength:
        underLength = False
        newPrev = []
        for part in prev:
            for towel in towels:
                temp = part + towel
                if len(temp) > length and not underLength:
                    underLength = False
                else:
                    underLength = True
                allPossible[temp] = True
                newPrev.append(temp)
        prev = newPrev

    return allPossible


with open("./input.txt") as f:
    result = 0
    towels = []
    patterns = []
    readingTowels = True
    longest = 0

    for line in f:
        input = line.strip()
        if input == "":
            readingTowels = False
        elif readingTowels:
            towels = input.split(", ")
        else:
            if len(input) > longest:
                longest = len(input)
            patterns.append(input)

    # print(longest)
    # allPossible = generatePossibilities(towels, longest)
    # print(allPossible)
    towelMap = generateMap(towels)

    # print(towels)
    # print(patterns)
    # for pattern in patterns:
    #     if pattern in allPossible:
    #         result += 1

    count = 1
    for pattern in patterns:
        print(count)
        if canMatch2(pattern, towelMap):
            result += 1
        count += 1

    print(result)
