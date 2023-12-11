from multiprocessing import Pool


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

def expandCol(universe):
    for idx in reversed(range(len(universe[0]))):
        empty = True
        for row in universe:
            if not (row[idx] == "." or row[idx] == "*"):
                empty = False
        
        if empty:
            for id2, row in enumerate(universe):
                universe[id2] = replacer(row, "*", idx)
    
    return universe

def expandRow(universe):
    newUniverse = []
    for row in universe:
        empty = True
        for col in row:
            if not (col == "." or col == "*"):
                empty = False
        if empty:
            blank = "*" * len(row)
            newUniverse.append(blank)
        else:
            newUniverse.append(row)
    
    return newUniverse

def expand(universe):
    universe = expandCol(universe)
    return expandRow(universe)

def findGalaxies(universe, galaxies):
    for id1, row in enumerate(universe):
        for id2, val in enumerate(row):
            if val == "#":
                galaxies.append((id1, id2))

    return galaxies

def getPairs(galaxies, universe):
    pairs = []
    for idx, start in enumerate(galaxies):
        left = []
        right = []
        for end in galaxies[idx+1:]:
            if (end[1] < start[1]):
                left.append(end)
            else:
                right.append(end)
        pairs.append([start, right, universe])
        pairs.append([start, left, universe])
    return pairs

def findEdges(start, ends):
    rl = start[0]
    rh = start[0]
    cl = start[1]
    ch = start[1]

    for val in ends:
        if val[0] < rl:
            rl = val[0]
        if val[0] > rh:
            rh = val[0]
        if val[1] < cl:
            cl = val[1]
        if val[1] > ch:
            ch = val[1]
    
    return rl, rh, cl, ch

def shortestPath(temp):
    queue = []
    visited = {}
    start = temp[0]
    ends = temp[1]
    universe = temp[2]
    # print("starting:", start, end)
    rl, rh, cl, ch = findEdges(start, ends)
    visited[start] = True
    # Mark all the vertices as not visited
    queue.append((start, 0))
    total = 0

    while queue:
        curr, dist = queue.pop(0)
        if curr in ends:
            # print("found:", start, curr, dist)
            total += dist
            ends.remove(curr)
            # print("ends:", ends)
            if len(ends) == 0:
                return total
        if curr[1] > cl:
            new = (curr[0], curr[1] - 1)
            if new not in visited:
                visited[new] = True
                if universe[new[0]][new[1]] == '*':
                    queue.append((new, dist + 1000000))
                else:
                    queue.append((new, dist + 1))
        if curr[0] < rh:
            new = (curr[0] + 1, curr[1])
            if new not in visited:
                visited[new] = True
                if universe[new[0]][new[1]] == '*':
                    queue.append((new, dist + 1000000))
                else:
                    queue.append((new, dist + 1))
        if curr[1] < ch:
            new = (curr[0], curr[1] + 1)
            if new not in visited:
                visited[new] = True
                if universe[new[0]][new[1]] == '*':
                    queue.append((new, dist + 1000000))
                else:
                    queue.append((new, dist + 1))
    
    return total

if __name__ == '__main__':
    result = 0
    galaxies = []
    universe = []
    pairs = {}
    with open('./input.txt') as f:
        for line in f:
            universe.append(line.strip())

    universe = expand(universe)
    galaxies = findGalaxies(universe, galaxies)
    pairs = getPairs(galaxies, universe)
    print(len(pairs))

    with Pool(processes=None) as pool: 
        results = pool.map(shortestPath, pairs)
        #close the pool and wait for the work to finish
        pool.close()
        pool.join()

    # print(results)
    for val in results:
        result += val

    # for pair in pairs:
    #     print(pair)
    #     result += shortestPath(pair, universe)

    print(result)
