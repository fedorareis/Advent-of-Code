def preprocess(line):
    conversion = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    result = line
    for k, v in conversion.items():
        result = result.replace(k, v)

    return result

with open('./input.txt') as f:
    result = 0
    for line in f:
        first = 0
        last = 0
        found_first = False
        processed = preprocess(line)
        for val in processed:
            try:
                curr = int(val)
                if not found_first:
                    first = val
                    last = val
                    found_first = True
                else:
                    last = val
            except:
                pass
        
        result += int(first + "" + last)

    print(result)
