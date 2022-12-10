with open('./input.txt') as f:
    register = 1
    cycleTotal = 1
    result = ""
    scan = 0
    for line in f:
        line = line.strip()
        ops = line.split(" ")
        cycles = 0
        val = 0
        if ops[0] == "noop":
            cycles = 1
        elif ops[0] == "addx":
            cycles = 2
            val = int(ops[1])

        while cycles > 0:
            if scan >= register - 1 and scan <= register + 1:
                result += "#"
            else:
                result += "."

            scan += 1
            if cycleTotal % 40 == 0:
                print(result)
                result = ""
                scan = 0
            cycles += -1
            cycleTotal += 1

        register += val
