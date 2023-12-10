exStart = [(1, 1), "F", "below"]
ex2Start = [(2, 0), "F", "below"]
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

pipe = {
    "|": {
        "below": up,
        "above": down,
    },
    "-": {
        "left": right,
        "right": left,
    },
    "L": {
        "right": up,
        "above": right,
    },
    "J": {
        "left": up,
        "above": left,
    },
    "7": {
        "left": down,
        "below": left,
    },
    "F": {
        "right": down,
        "below": right,
    }
}

def traverse(start, pipes):
    coord = start[0]
    tile = start[1]
    direction = start[2]
    count = 0

    while tile != "S":
        # print(tile)
        count += 1
        tile, coord, direction = pipe[tile][direction](pipes, coord)

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

    print(traverse(inputStart, pipes)/2)
