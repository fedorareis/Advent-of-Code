conversion = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

with open('./input.txt') as f:
    result = 0
    for line in f:
        first = {
            "val": 0,
            "index": len(line),
        }
        last = {
            "val": 0,
            "index": 0,
        }
        found_first = False
        
        for k, v in conversion.items():
            idx = line.find(k)
            lidx = line.rfind(k)
            if idx >= 0 and idx <= first["index"]:
                first["index"] = idx
                first["val"] = v
            if lidx >= 0 and lidx >= last["index"]:
                last["index"] = lidx
                last["val"] = v

        for idx, val in enumerate(line):
            try:
                curr = int(val)
                if idx <= first["index"]:
                    first["index"] = idx
                    first["val"] = curr
                if idx >= last["index"]:
                    last["index"] = idx
                    last["val"] = curr
            except:
                pass
        
        result += int(str(first["val"]) + str(last["val"]))

    print(result)
