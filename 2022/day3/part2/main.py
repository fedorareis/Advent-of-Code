with open('./input.txt') as f:
    result = 0
    items = {}
    idx = 1
    for line in f:
        line = line.strip()
        for char in line:
            if idx == 1:
                items[char] = False
            elif idx == 2:
                if char in items:
                    items[char] = True
            else:
                if char in items and items[char]:
                    val = 0
                    if char.isupper():
                        val = ord(char) - 38
                    else:
                        val = ord(char) - 96
                    result += val
                    items = {}
                    idx = 0
                    break
        idx += 1

    print(result)
