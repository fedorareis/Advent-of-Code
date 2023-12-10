exStart = [(1, 1), "F", "below"]
ex2Start = [(2, 0), "F", "below"]
ex3Start = [(1, 1), "F", "below"]
ex4Start = [(4, 12), "F", "below"]
ex5Start = [(0, 5), "7", "below"]
ex6Start = [(1, 1), "F", "below"]
inputStart = [(38, 55), "|", "below"]

def up(tiles, coord):
    newCoord = (coord[0]-1, coord[1])
    return tiles[newCoord[0]][newCoord[1]], newCoord, "below"

def down(tiles, coord):
    newCoord = (coord[0]+1, coord[1])
    return tiles[newCoord[0]][newCoord[1]], newCoord, "above"

def left(tiles, coord):
    newCoord = (coord[0], coord[1]-1)
    return tiles[newCoord[0]][newCoord[1]], newCoord, "right"

def right(tiles, coord):
    newCoord = (coord[0], coord[1]+1)
    return tiles[newCoord[0]][newCoord[1]], newCoord, "left"

def getSide(curr, mod):
    sides = ["bottom", "left", "top", "right"]
    new = (curr + mod) % 4

    return sides[new], new

pipe = {
    "|": {
        "below": (up, 0),
        "above": (down, 0),
    },
    "-": {
        "left": (right, 0),
        "right": (left, 0),
    },
    "L": {
        "right": (up, 1),
        "above": (right, -1),
    },
    "J": {
        "left": (up, -1),
        "above": (left, 1),
    },
    "7": {
        "left": (down, 1),
        "below": (left, -1),
    },
    "F": {
        "right": (down, -1),
        "below": (right, 1),
    }
}

found = {}

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def markFound(coord):
    if coord[0] in found:
        found[coord[0]][coord[1]] = True
    else:
        temp = {}
        temp[coord[1]] = True
        found[coord[0]] = temp

def removePipe(pipes):
    for id1, row in enumerate(pipes):
        for id2, col in enumerate(row):
            if not (id1 in found and id2 in found[id1]):
                pipes[id1] = replacer(pipes[id1], ".", id2)
    
    return pipes

def clearOuter(pipes):
    queue = []
    for idx, val in enumerate(pipes[0]):
        if val == '.':
            pipes[0] = replacer(pipes[0], " ", idx)
            if pipes[1][idx] == '.':
                queue.append((1, idx))
    
    while len(queue) > 0:
        temp = queue.pop(0)
        if pipes[temp[0]][temp[1]] != " ":
            pipes[temp[0]] = replacer(pipes[temp[0]], " ", temp[1])

            if temp[0] > 0:
                if pipes[temp[0] - 1][temp[1]] == '.':
                    queue.append((temp[0] - 1, temp[1]))

            if temp[1] > 0:
                if pipes[temp[0]][temp[1] - 1] == '.':
                    queue.append((temp[0], temp[1] - 1))

            if temp[0] < len(pipes) - 1:
                if pipes[temp[0] + 1][temp[1]] == '.':
                    queue.append((temp[0] + 1, temp[1]))

            if temp[1] < len(pipes[temp[0]]) - 1:
                if pipes[temp[0]][temp[1] + 1] == '.':
                    queue.append((temp[0], temp[1] + 1))

    return pipes

def traverse(start, pipes):
    coord = start[0]
    tile = start[1]
    direction = start[2]
    count = 0

    while tile != "S":
        count += 1
        tile, coord, direction = pipe[tile][direction][0](pipes, coord)
        markFound(coord)

    pipes[coord[0]] = replacer(pipes[coord[0]], start[1], coord[1])

    return pipes

def travOutside(pipes):
    tile, start = findOuterStart(pipes)
    coord = start
    direction = "below" # start will always be an F
    side = "left"
    sideIdx = 1
    init = True

    while coord != start or init:
        init = False

        pipes = removeAdj(pipes, side, coord)
        
        side, sideIdx = getSide(sideIdx, pipe[tile][direction][1])
        pipes = removeAdj(pipes, side, coord)
        tile, coord, direction = pipe[tile][direction][0](pipes, coord)
    
    return pipes

def removeAdj(pipes, side, coord):
    if side == "left" and coord[1] > 0:
        if pipes[coord[0]][coord[1]-1] == '.':
            pipes[coord[0]] = replacer(pipes[coord[0]], " ", coord[1]-1)
    elif side == "top" and coord[0] > 0:
        if pipes[coord[0]-1][coord[1]] == '.':
            pipes[coord[0] - 1] = replacer(pipes[coord[0] - 1], " ", coord[1])
    elif side == "bottom" and coord[0] < len(pipes) - 1:
        if pipes[coord[0]+1][coord[1]] == '.':
            pipes[coord[0] + 1] = replacer(pipes[coord[0] + 1], " ", coord[1])
    elif side == "right" and coord[1] < len(pipes[coord[0]]) - 1:
        if pipes[coord[0]][coord[1]+1] == '.':
            pipes[coord[0]] = replacer(pipes[coord[0]], " ", coord[1]+1)

    return pipes
        
def findOuterStart(pipes):
    for id1, row in enumerate(pipes):
        for id2, tile in enumerate(row):
            if tile != " ":
                return tile, (id1, id2)
            
def countInside(pipes):
    count = 0
    for row in pipes:
        for tile in row:
            if tile == ".":
                count += 1
    return count

with open('./input.txt') as f:
    result = 0
    coord = (0,0)
    pipes = []

    for idx, line in enumerate(f):
        line = line.strip()
        start = line.find("S")
        if start != -1:
            coord = (idx, start)
        pipes.append(line)

    pipes = traverse(inputStart, pipes)
    pipes = removePipe(pipes)
    pipes = clearOuter(pipes)
    pipes = travOutside(pipes)
    result = countInside(pipes)

    print(result)
