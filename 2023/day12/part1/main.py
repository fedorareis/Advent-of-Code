if __name__ == '__main__':
    result = 0

    with open('./input.txt') as f:
        for line in f:
            line = line.strip()
            for val in line:
                result += val

    print(result)
