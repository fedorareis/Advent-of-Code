def moveRope(rope):
    res = rope.copy()
    idx = 1
    while idx < len(res):
        # I really didn't want to keep track of the references throughout the logic
        # plus this allowed me to just drop in the logic from part 1. :)
        hx = res[idx-1][0]
        hy = res[idx-1][1]
        tx = res[idx][0]
        ty = res[idx][1]
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
        res[idx][0] = tx
        res[idx][1] = ty
        idx += 1
    return res


with open('./input.txt') as f:
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
            [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visited = {}
    result = 0
    for line in f:
        line = line.strip()
        (direction, spaces) = line.split(" ")
        spaces = int(spaces)
        while spaces > 0:
            if direction == "U":
                rope[0][1] += 1
            if direction == "D":
                rope[0][1] += -1
            if direction == "R":
                rope[0][0] += 1
            if direction == "L":
                rope[0][0] += -1
            rope = moveRope(rope)
            spaces += -1

            key = '[%d, %d]' % (rope[9][0], rope[9][1])
            visited[key] = True

    print(len(visited))
