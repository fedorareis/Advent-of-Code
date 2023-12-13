import math
import re

def group(springs):
    groups = []

    temp = ""
    for val in springs:
        if val != ".":
            temp += val
        if len(temp) > 0 and val == ".":
            groups.append(temp)
            temp = ""
    if len(temp) > 0:
        groups.append(temp)
    return groups

def splitDamaged(group):
    groups = []

    temp = ""
    for val in group:
        if val == "#":
            temp += val
        if len(temp) > 0 and val != "#":
            groups.append(temp)
            temp = ""
    if len(temp) > 0:
        groups.append(temp)
    return groups

def arrange(group, rule):
    dGroups = splitDamaged(group)

    if len(dGroups) == 1 and len(dGroups[0]) == rule:
        return 1
    
    if len(dGroups) == 0:
        return math.ceil(len(group)/ rule)
    
def arrangeOdd(groups, rules):
    count = 0

    if len(groups) == 1:
        if len(groups[0]) - sum(rules) == 1:
            return 1
        
    return count

def evenGrouping(groups, rules):
    count = 0

    newGroups = []
    newRules = []
    for idx, val in enumerate(groups):
        if len(val) != rules[idx]:
            # print(len(val), rules[idx])
            newGroups.append(val)
            newRules.append(rules[idx])
    groups = newGroups
    rules = newRules

    if len(groups) == 0:
        return 1
    
    for idx, val in enumerate(groups):
        count += arrange(val, rules[idx])

    print(groups, rules, count)
    return count

def oddGrouping(groups, rules):
    count = 0

    if len(groups) > 1:
        newGroups = groups
        newRules = rules
        for idx, group in enumerate(groups):
            if len(group) != rules[idx]:
                newGroups = groups[idx:]
                newRules = rules[idx:]
                break

        if len(newGroups) > 1:
            for idx, group in reversed(list(enumerate(newGroups))):
                offset = (len(groups) - idx)
                if len(group) != newRules[-offset]:
                    if offset == 1:
                        break
                    newGroups = newGroups[:idx+1]
                    newRules = newRules[:-(offset-1)]
                    break

        print("new:", newGroups, newRules, "original:" ,groups, rules)
        count += arrangeOdd(newGroups, newRules)
        

    return count

def arrangements(springs, rules):
    count = 0
    groups = group(springs)
    rules = [int(x) for x in rules.split(",")]

    if len(groups) == len(rules):
        count += evenGrouping(groups, rules)
    else:
        count += oddGrouping(groups, rules)

    return count

if __name__ == '__main__':
    result = 0

    with open('./ex.txt') as f:
        for line in f:
            line = line.strip()
            springs, rules = line.split(" ")
            result += arrangements(springs, rules)

    print(result)
