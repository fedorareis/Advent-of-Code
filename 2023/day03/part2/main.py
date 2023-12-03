import re

schema = []

def preprocess(file):
    schematic = []
    for line in file:
        line = line.strip()
        schematic.append(line)
    
    return schematic

def FindAllAdjacent(row, idx, y, schema):
    results = []
    for item in row:
        num = int(schema[y][item[0]:item[1]+1])
        if idx - 1 == item[1]:
            results.append(num)
        if idx + 1 == item[0]:
            results.append(num)
        if idx >= item[0] and idx <= item[1]:
            results.append(num)
    return results

with open('./input.txt') as f:
    result = 0
    schema = preprocess(f)

    gears = []
    nums = []

    for row in schema:
        gears.append([m.start(0) for m in re.finditer("\*", row)])
        nums.append([(m.start(0), m.end(0)-1) for m in re.finditer("\d+", row)])
    
    for y, row in enumerate(gears):
        for x in row:
            temp = []
            if y > 0:
                temp = temp + FindAllAdjacent(nums[y-1], x, y-1, schema)
            if y < len(schema) - 1:
                temp = temp + FindAllAdjacent(nums[y+1], x, y+1, schema)
            temp = temp + FindAllAdjacent(nums[y], x, y, schema)

            if len(temp) == 2:
                result += (temp[0] * temp[1])

    print(result)
