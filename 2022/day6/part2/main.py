with open('./input.txt') as f:
    result = 0
    for line in f:
        for idx in range(0, len(line)-14):
            found = True
            letters = set()
            for char in line[idx:idx+14]:
                if char not in letters:
                    letters.update(char)
                else:
                    found = False
                    break
            if found:
                result = idx+14
                break

    print(result)
