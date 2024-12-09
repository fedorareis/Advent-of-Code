def isSafe(start, end, increasing):
    change = start - end

    if change > 0 and change <= 3 and not increasing:
        return True

    if change < 0 and change >= -3 and increasing:
        return True

    return False


def isIncreasing(start, end):
    if end - start > 0:
        return True

    return False


with open("./input.txt") as f:
    result = 0
    for line in f:
        line = line.strip()
        increasing = False
        damper = False
        skip = False
        val = line.split(" ")

        for i in range(len(val) - 1):
            if skip:
                skip = False
                continue

            start = int(val[i])
            end = int(val[i + 1])
            if i == 0 and isIncreasing(start, end):
                increasing = True

            if isSafe(start, end, increasing):
                if i == len(val) - 2:
                    result += 1
                continue
            else:
                if not damper:
                    damper = True
                    # If we are at the end of the list
                    if i == len(val) - 2:
                        result += 1
                        break

                    # check after next number when next number has problem
                    if i + 2 < len(val):
                        start = int(val[i])
                        end = int(val[i + 2])
                        if i == 0:
                            increasing = False
                            if isIncreasing(start, end):
                                increasing = True
                    if isSafe(start, end, increasing):
                        if i + 2 == len(val) - 1:
                            result += 1
                            break
                        skip = True
                        continue

                    # check before current number if current number has problem
                    if i > 0:
                        start = int(val[i - 1])
                        end = int(val[i + 1])
                    if isSafe(start, end, increasing):
                        if i == len(val) - 2:
                            result += 1
                            break
                        continue

                    # drop first if first has problem
                    if i == 0:
                        start = int(val[i + 1])
                        end = int(val[i + 2])
                        increasing = False
                        if isIncreasing(start, end):
                            increasing = True
                        continue

                    if i == 1:
                        start = int(val[i])
                        end = int(val[i + 1])
                        increasing = False
                        if isIncreasing(start, end):
                            increasing = True
                        if isSafe(start, end, increasing):
                            if i == len(val) - 2:
                                result += 1
                                break
                            continue

                print(val, i, increasing)
                break

    print(result)
