with open('./input.txt') as f:
    result = 0
    dirs = {}
    curr_dirs = [""]
    for line in f:
        line = line.strip()
        vals = line.split(" ")
        if vals[0] == "$":
            if vals[1] == "cd":
                if vals[2] == "..":
                    curr_dirs.pop()
                elif vals[2] == "/":
                    curr_dirs = [""]
                else:
                    curr_dirs.append(vals[2])

        else:
            if vals[0].isnumeric():
                size = int(vals[0])
                temp = curr_dirs.copy()
                while len(temp) > 0:
                    key = "/".join(temp)
                    if key in dirs:
                        dirs[key] += size
                    else:
                        dirs[key] = size
                    temp.pop()

    for d, s in dirs.items():
        if s <= 100000:
            result += s

    print(result)
