import re

schema = []

def preprocess(file):
    schematic = []
    for line in file:
        line = line.strip()
        schematic.append(line)
    
    return schematic

def isAdjacent(row, item):
    for idx in row:
        if idx - 1 == item[1]:
            return True
        if idx + 1 == item[0]:
            return True
        if idx >= item[0] and idx <= item[1]:
            return True
    return False

with open('./input.txt') as f:
    result = 0
    schema = preprocess(f)

    symbols = []
    nums = []

    for row in schema:
        symbols.append([m.start(0) for m in re.finditer("[^\d.]", row)])
        nums.append([(m.start(0), m.end(0)-1) for m in re.finditer("\d+", row)])
    
    for y, row in enumerate(nums):
        for item in row:
            num = int(schema[y][item[0]:item[1]+1])
            if y > 0:
                if isAdjacent(symbols[y-1], item):
                    result += num
                    continue
            if y < len(schema) - 1:
                if isAdjacent(symbols[y+1], item):
                    result += num
                    continue
            if isAdjacent(symbols[y], item):
                result += num

    print(result)
