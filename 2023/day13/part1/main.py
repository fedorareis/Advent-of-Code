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
