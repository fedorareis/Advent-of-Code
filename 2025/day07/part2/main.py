from pprint import pprint


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def traverse(root, routes):
    if root is None:
        return routes + 1
    # print(root.val)

    routes = traverse(root.left, routes)
    return traverse(root.right, routes)


with open("./input.txt") as f:
    result = 0
    map = []
    lookup = {}
    prev = ""
    row = -1
    for line in f:
        row += 1
        line = line.strip()
        if prev == "":
            prev = line
            map.append(list(line))
            continue

        line = list(line)
        for i in range(len(line)):
            if prev[i] == "S":
                lookup["S"] = Node(str(row - 1) + "," + str(i))
                line[i] = "|"

            if prev[i] == "|":
                if line[i] == "^":
                    currentNode = Node(str(row) + "," + str(i))
                    line[i - 1] = "|"
                    line[i + 1] = "|"
                    for j in range(row - 1, -1, -1):
                        if map[j][i] == "." or map[j][i] == "^":
                            break
                        if map[j][i] == "S":
                            lookup["S"] = currentNode
                            break
                        if (
                            i > 0
                            and map[j][i - 1] == "^"
                            and str(j) + "," + str(i - 1) in lookup
                        ):
                            lookup[str(j) + "," + str(i - 1)].right = currentNode
                        if (
                            i < len(line)
                            and map[j][i + 1] == "^"
                            and str(j) + "," + str(i + 1) in lookup
                        ):
                            lookup[str(j) + "," + str(i + 1)].left = currentNode
                    lookup[str(row) + "," + str(i)] = currentNode
                else:
                    line[i] = "|"
        prev = "".join(line)
        map.append(line)
    # pprint(map)
    print("finished building tree")
    result = traverse(lookup["S"], 0)

    print(result)

# for i in range(len(line)):
#         if prev[i] == "S":
#             line[i] = "|"

#         if prev[i] == "|":
#             if line[i] == "^":
#                 line[i - 1] = "|"
#                 line[i + 1] = "|"
#                 result += 1
#             else:
#                 line[i] = "|"
