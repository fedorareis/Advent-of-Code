import itertools
import more_itertools
import pprint


def addParens(expr):
    skip = True
    count = (expr.count("+") + expr.count("*")) - 1

    expr = ("(" * count) + expr
    idx = 0
    if count > 0:
        while idx < len(expr):
            char = expr[idx]
            if char == "+" or char == "*":
                if skip:
                    skip = False
                    idx += 1
                    continue
                expr = expr[:idx] + ")" + expr[idx:]
                idx += 1  # extra increment to offset new char
            idx += 1

    return expr


def mutations(values):
    results = []

    for val in itertools.product("+*|", repeat=len(values) - 1):
        expr = "".join(list(more_itertools.interleave_longest(values, val)))
        # print(expr)
        temp = []
        for val in expr.split("|"):
            temp.append(addParens(val))
        expr = "|".join(temp)
        results.append(expr)
        # print(expr)

    # pprint.pprint(results)
    return results


def eval(expr):
    # TODO: finish function. Maybe recursion?
    skip = True
    count = (expr.count("+") + expr.count("*")) - 1

    expr = ("(" * count) + expr
    idx = 0
    if count > 0:
        while idx < len(expr):
            char = expr[idx]
            if char in "+*|":
                if skip:
                    skip = False
                    idx += 1
                    continue
                temp = str(eval(expr[:idx]))
                if char == "|":
                    expr = temp + expr[idx + 1 :]
                else:
                    expr = expr[:idx] + expr[idx:]
            idx += 1

    return expr


def calc(res, terms):
    for expr in mutations(terms):
        # print(res, expr)
        temp = []
        for val in expr.split("|"):
            temp.append(str(eval(val)))
        calc = int("".join(temp))
        print(res, expr, "=", calc)
        if int(res) == calc:
            print("found:", res)
            return int(res)

    return 0


with open("./ex.txt") as f:
    result = 0

    for line in f:
        val = line.strip().split(": ")
        # pprint.pprint(val[1])
        result += calc(val[0], val[1].split(" "))

    print(result)
