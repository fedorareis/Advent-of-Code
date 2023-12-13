def verticalReflect(field):
    field2 = []
    id2 = 0
    rIdx = 0
    reflect = False

    for idx in range(len(field[0])):
        col = ""
        for row in field:
            col += row[idx]

        if not reflect:
            if id2 > 0 and col == field2[-1]:
                reflect = True
                rIdx = id2
        else:
            offset = (id2 - rIdx) + 1
            if rIdx - offset < 0:
                break
            if col != field2[rIdx - offset]:
                reflect = False
        field2.append(col)
        id2 += 1

    if reflect:
        return rIdx
    return 0

def lineComp(line1, line2, toggle):
    if line1 == line2:
        return True, False
    
    if toggle:
        match = True
        flip = False
        for idx in range(len(line1)):
            if line1[idx] != line2[idx]:
                if not flip:
                    flip = True
                else:
                    return False, False
        
        return match, flip

if __name__ == '__main__':
    result = 0

    with open('./input.txt') as f:
        field = []
        idx = 0
        rIdx = 0
        reflect = False
        for line in f:
            line = line.strip()
            if line == "":
                if reflect:
                    result += (rIdx) * 100
                else:
                    result += verticalReflect(field)

                field = []
                rIdx = 0
                idx = 0
                reflect = False
            else:
                if not reflect:
                    # This probably won't work because I would need to be able to iterate across the field on failure to see if another point is a viable mirror index
                    eq, flip = lineComp(line, field[-1], True)
                    if idx > 0 and line == field[-1]:
                        reflect = True
                        rIdx = idx
                else:
                    offset = (idx - rIdx) + 1
                    if rIdx - offset >= 0:
                        if line != field[rIdx - offset]:
                            reflect = False
                field.append(line)
                idx += 1

        if reflect:
            result += (rIdx) * 100
        else:
            result += verticalReflect(field)

    print(result)
