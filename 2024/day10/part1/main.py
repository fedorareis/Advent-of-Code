import pprint


def search(input, x, y):
    queue = [{"val": 0, "x": x, "y": y}]
    count = 0
    visited = {}

    while len(queue) > 0:
        current = queue.pop(0)
        val = current["val"]
        x = current["x"]
        y = current["y"]

        if val == 9 and "{},{}".format(x, y) not in visited:
            count += 1
            visited["{},{}".format(x, y)] = True
            continue

        visited["{},{}".format(x, y)] = True

        if (
            y > 0
            and input[y - 1][x] == val + 1
            and not "{},{}".format(x, y - 1) in visited
        ):
            queue.append({"val": input[y - 1][x], "x": x, "y": y - 1})

        if (
            x > 0
            and input[y][x - 1] == val + 1
            and not "{},{}".format(x - 1, y) in visited
        ):
            queue.append({"val": input[y][x - 1], "x": x - 1, "y": y})

        if (
            y < len(input) - 1
            and input[y + 1][x] == val + 1
            and not "{},{}".format(x, y + 1) in visited
        ):
            queue.append({"val": input[y + 1][x], "x": x, "y": y + 1})

        if (
            x < len(input[y]) - 1
            and input[y][x + 1] == val + 1
            and not "{},{}".format(x + 1, y) in visited
        ):
            queue.append({"val": input[y][x + 1], "x": x + 1, "y": y})

        # print("x:", x, "y:", y, "val:", val, "queue:", queue)

    # print(count)
    return count


with open("./input.txt") as f:
    result = 0
    input = []
    y = 0
    x = 0

    for line in f:
        val = line.strip()
        input.append([int(x) for x in list(val)])

    for row in input:
        x = 0
        for val in row:
            if val == 0:
                result += search(input, x, y)
            x += 1
        y += 1

    print(result)
