ex = [
    {
        "time": 71530,
        "dist": 940200,
    }
]

input = [
    {
        "time": 54946592,
        "dist": 302147610291404,
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

    for race in input:
        min = least(race)
        max = most(race)
        result *= (max - min) + 1

    print(result)
