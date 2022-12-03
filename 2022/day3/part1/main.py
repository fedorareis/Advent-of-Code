with open('./input.txt') as f:
    result = 0
    items = {}
    for line in f:
        line = line.strip()
        idx = 0
        for char in line:
            if idx < len(line)/2:
                items[char] = True
            else:
                if char in items:
                    val = 0
                    if char.isupper():
                        val = ord(char) - 38
                    else:
                        val = ord(char) - 96
                    result += val
                    items = {}
                    break
            idx += 1

    print(result)
