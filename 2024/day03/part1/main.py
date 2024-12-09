import re


def parse(item):
    val = re.findall(r"\d{1,3},\d{1,3}", item)
    nums = val[0].split(",")
    return nums


with open("./input.txt") as f:
    result = 0
    for line in f:
        val = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for item in val:
            nums = parse(item)
            result += int(nums[0]) * int(nums[1])

    print(result)
