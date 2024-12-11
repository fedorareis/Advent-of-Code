import pprint


def blink(input):
    output = []

    # print("input:", input)
    for rock in input:
        if rock == "0":
            output.append("1")
            continue
        if len(rock) % 2 == 0:
            output.append(str(int(rock[: int(len(rock) / 2)])))
            output.append(str(int(rock[int(len(rock) / 2) :])))
            continue
        else:
            output.append(str(int(rock) * 2024))
            continue
    # print("output:", output)
    return output


with open("./input.txt") as f:
    result = 0
    input = []
    blinks = 25

    for line in f:
        input = line.strip().split(" ")

    while blinks > 0:
        input = blink(input)
        blinks = blinks - 1

    print(len(input))
