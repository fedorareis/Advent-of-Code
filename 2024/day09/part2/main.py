import pprint

with open("./input.txt") as f:
    result = 0
    input = []
    fs = []

    for line in f:
        val = line.strip()
        input = list(val)

    id = 0
    for index, value in enumerate(input):
        value = int(value)
        if index % 2 == 0:
            fs.append({"id": id, "moved": False, "empty": False, "length": value})
            id += 1
        else:
            if value != 0:
                fs.append({"id": None, "moved": False, "empty": True, "length": value})

    end = len(fs) - 1
    while end > 0:
        # pprint.pprint(fs)
        temp = fs[end]
        if not temp["empty"]:
            if temp["moved"]:
                end = end - 1
                continue

            start = 0
            while start <= end:
                sVal = fs[start]
                if sVal["empty"] and sVal["length"] > 0:
                    if sVal["length"] == temp["length"]:
                        # print("swap:", sVal, " and ", temp)
                        fs[end] = sVal
                        temp["moved"] = True
                        fs[start] = temp

                        if end < len(fs) - 1 and fs[end + 1]["empty"]:
                            fs[end]["length"] = (
                                fs[end]["length"] + fs[end + 1]["length"]
                            )
                            fs.pop(end + 1)

                        if fs[end - 1]["empty"]:
                            fs[end]["length"] = (
                                fs[end]["length"] + fs[end - 1]["length"]
                            )
                            fs.pop(end - 1)
                            end = end - 1
                        break
                    if sVal["length"] > temp["length"]:
                        # print("move ", temp, " to ", start)
                        fs.insert(
                            start + 1,
                            {
                                "id": None,
                                "moved": False,
                                "empty": True,
                                "length": sVal["length"] - temp["length"],
                            },
                        )
                        end += 1  # this counteracts the record that was inserted

                        temp["moved"] = True
                        fs[start] = temp
                        fs[end] = {
                            "id": None,
                            "moved": False,
                            "empty": True,
                            "length": temp["length"],
                        }

                        if end < len(fs) - 1 and fs[end + 1]["empty"]:
                            fs[end]["length"] = (
                                fs[end]["length"] + fs[end + 1]["length"]
                            )
                            fs.pop(end + 1)

                        if fs[end - 1]["empty"]:
                            fs[end]["length"] = (
                                fs[end]["length"] + fs[end - 1]["length"]
                            )
                            fs.pop(end - 1)
                            end = end - 1
                        break
                start += 1
        end = end - 1

    # pprint.pprint(fs)
    idx = 0
    for val in fs:
        count = val["length"]

        if val["empty"]:
            idx += count
            continue

        while count > 0:
            temp = idx * int(val["id"])
            # print(temp)
            result += temp
            count = count - 1
            idx += 1

    print(result)

# 6321642388129 : low
