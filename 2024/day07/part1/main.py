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

    for val in itertools.product("+*", repeat=len(values) - 1):
        expr = "".join(list(more_itertools.interleave_longest(values, val)))
        expr = addParens(expr)
        results.append(expr)

    return results


def calc(res, terms):
    for expr in mutations(terms):
        calc = eval(expr)
        if int(res) == calc:
            return int(res)

    return 0


with open("./input.txt") as f:
    result = 0

    for line in f:
        val = line.strip().split(": ")
        result += calc(val[0], val[1].split(" "))

    print(result)
