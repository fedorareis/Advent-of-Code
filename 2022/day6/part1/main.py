with open('./input.txt') as f:
    result = 0
    for line in f:
        for idx in range(0, len(line)-4):
            found = True
            letters = set()
            for char in line[idx:idx+4]:
                if char not in letters:
                    letters.update(char)
                else:
                    found = False
                    break
            if found:
                result = idx+4
                break

    print(result)
