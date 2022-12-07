with open('./input.txt') as f:
    filesystem = 70000000
    result = filesystem
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

    remaining = filesystem - dirs[""]
    for d, s in dirs.items():
        if s + remaining >= 30000000 and s < result:
            result = s

    print(result)
