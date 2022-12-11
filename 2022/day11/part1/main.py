import operator
ops = {"+": operator.add, "*": operator.mul}


def processInput(input):
    data = {"total": 0}
    arr = input.split("\n")

    # process Monkey
    val = arr[0].strip().split("Monkey ")
    data["monkey"] = int(val[1].strip().split(":")[0])

    # process Starting Items
    val = arr[1].strip().split("Starting items: ")
    val = val[1].strip().split(", ")
    data["items"] = list(map(int, val))

    # process Operation
    val = arr[2].strip().split("Operation: new = old ")
    val = val[1].strip().split(" ")
    data["operation"] = lambda a: ops[val[0]](
        a, int(val[1])) if val[1] != "old" else ops[val[0]](a, a)

    # process Test
    test = int(arr[3].strip().split("Test: divisible by ")[1])
    true = int(arr[4].strip().split("If true: throw to monkey ")[1])
    false = int(arr[5].strip().split("If false: throw to monkey ")[1])
    data["test"] = lambda a: true if a % test == 0 else false

    return data


with open('./input.txt') as f:
    result = 0
    rounds = 1
    monkeys = []
    bufferedInput = ""
    for line in f:
        if line == "\n":
            value = processInput(bufferedInput)
            monkeys.append(value)
            bufferedInput = ""
        else:
            bufferedInput += line
    value = processInput(bufferedInput)
    monkeys.append(value)
    bufferedInput = ""

    while rounds <= 20:
        for monkey in monkeys:
            while len(monkey["items"]):
                monkey["total"] += 1
                item = monkey["items"].pop(0)
                item = monkey["operation"](item)
                item = item // 3
                goto = monkey["test"](item)
                monkeys[goto]["items"].append(item)
        rounds += 1

    def cond(a): return a["total"]
    monkeys.sort(key=cond, reverse=True)
    result = monkeys[0]["total"] * monkeys[1]["total"]

    print(result)
