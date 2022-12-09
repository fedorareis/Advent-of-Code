def moveTail(hx, hy, tx, ty):
    if hx > tx and hx - tx > 1:
        if hy > ty:
            ty += 1
        if ty > hy:
            ty += -1
        tx += 1
    if tx > hx and tx - hx > 1:
        if hy > ty:
            ty += 1
        if ty > hy:
            ty += -1
        tx += -1
    if hy > ty and hy - ty > 1:
        if hx > tx:
            tx += 1
        if tx > hx:
            tx += -1
        ty += 1
    if ty > hy and ty - hy > 1:
        if hx > tx:
            tx += 1
        if tx > hx:
            tx += -1
        ty += -1
    return (tx, ty)


with open('./input.txt') as f:
    tx = 0
    ty = 0
    hx = 0
    hy = 0
    visited = {}
    result = 0
    for line in f:
        line = line.strip()
        (direction, spaces) = line.split(" ")
        spaces = int(spaces)
        while spaces > 0:
            if direction == "U":
                hy += 1
            if direction == "D":
                hy += -1
            if direction == "R":
                hx += 1
            if direction == "L":
                hx += -1
            (tx, ty) = moveTail(hx, hy, tx, ty)
            spaces += -1

            key = '[%d, %d]' % (tx, ty)
            visited[key] = True

    print(len(visited))
