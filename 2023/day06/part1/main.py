ex = [
    {
        "time": 7,
        "dist": 9,
    },
    {
        "time": 15,
        "dist": 40,
    },
    {
        "time": 30,
        "dist": 200,
    }
]

input = [
    {
        "time": 54,
        "dist": 302,
    },
    {
        "time": 94,
        "dist": 1476,
    },
    {
        "time": 65,
        "dist": 1029,
    },
    {
        "time": 92,
        "dist": 1404,
    }
]

def least(race):
    time = race["time"]
    for i in range(time):
        distance = (time - i) * i
        if distance > race["dist"]:
            return i
        
def most(race):
    time = race["time"]
    for i in reversed(range(time)):
        distance = (time - i) * i
        if distance > race["dist"]:
            return i

if __name__ == '__main__':
    result = 1

    for race in ex:
        min = least(race)
        max = most(race)
        result *= (max - min) + 1

    print(result)
