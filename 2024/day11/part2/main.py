import pprint
from multiprocessing import Pool


def blink(input):
    output = {}

    for rock in input.keys():

        if rock == "0":
            if "1" in output:
                output["1"] = output["1"] + input[rock]
            else:
                output["1"] = input[rock]
            continue
        if len(rock) % 2 == 0:
            first = str(int(rock[: int(len(rock) / 2)]))
            second = str(int(rock[int(len(rock) / 2) :]))
            if first in output:
                output[first] = output[first] + input[rock]
            else:
                output[first] = input[rock]

            if second in output:
                output[second] = output[second] + input[rock]
            else:
                output[second] = input[rock]
            continue
        else:
            mult = str(int(rock) * 2024)
            if mult in output:
                output[mult] = output[mult] + input[rock]
            else:
                output[mult] = input[rock]
            continue
    return output


def blinks(rock):
    rocks = {}
    rocks[rock] = 1
    num = 75
    while num > 0:
        rocks = blink(rocks)
        num = num - 1

    result = 0
    for val in rocks.values():
        result += val
    return result


if __name__ == "__main__":
    result = 0
    input = []
    with open("./input.txt") as f:

        for line in f:
            input = line.strip().split(" ")

    # This probably doesn't need to be parallelized
    with Pool(processes=None) as pool:
        results = pool.map(blinks, input)
        # close the pool and wait for the work to finish
        pool.close()
        pool.join()

    for val in results:
        result += val

    print(result)
