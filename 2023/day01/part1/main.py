with open('./input.txt') as f:
    result = 0
    for line in f:
        first = ""
        last = ""
        found_first = False
        for val in line:
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
