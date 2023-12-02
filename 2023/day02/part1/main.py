# only 12 red cubes, 13 green cubes, and 14 blue cubes
RED = 12
GREEN = 13
BLUE = 14

# ex - Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

with open('./input.txt') as f:
    result = 0
    for line in f:
        line = line.strip()
        temp = line.split(": ")
        id = int(temp[0].split(" ")[1])
        matches = temp[1].split("; ")
        possible = True
        for items in matches:
            if possible:
                r = 0
                g = 0
                b = 0
                for cubes in items.split(", "):
                    res = cubes.split(" ")
                    if res[1] == "red":
                        r += int(res[0])
                    elif res[1] == "green":
                        g += int(res[0])
                    elif res[1] == "blue":
                        b += int(res[0])
                
                if r > RED or g > GREEN or b > BLUE:
                    possible = False
        
        if possible:
            result += id
        
    print(result)
