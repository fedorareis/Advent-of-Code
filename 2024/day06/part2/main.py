import re

active = True


def parse(item):
    global active

    if item == "do()":
        active = True
        return [0, 0]
    if item == "don't()":
        active = False
        return [0, 0]

    if not active:
        return [0, 0]

    val = re.findall(r"\d{1,3},\d{1,3}", item)
    nums = val[0].split(",")
    return nums


with open("./input.txt") as f:
    result = 0
    for line in f:
        val = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line)
        for item in val:
            nums = parse(item)
            result += int(nums[0]) * int(nums[1])

    print(result)
