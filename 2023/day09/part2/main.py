def findHistory(list):
    result = []
    zeros = True
    for idx in range(0, len(list) - 1):
        temp = list[idx + 1] - list[idx]
        if temp != 0:
            zeros = False
        result.append(temp)
        idx += 1
    
    if zeros:
        return 0
    else:
        return result[0] - findHistory(result) 

with open('./input.txt') as f:
    result = 0

    for line in f:
        line = line.strip()
        temp = [int(x) for x in line.split(" ")]
        result += temp[0] - findHistory(temp)

    print(result)
