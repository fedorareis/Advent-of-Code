# ex - Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

with open('./input.txt') as f:
    result = 0
    for line in f:
        r = 0
        g = 0
        b = 0

        line = line.strip()
        temp = line.split(": ")
        matches = temp[1].split("; ")
        for items in matches:
            for cubes in items.split(", "):
                res = cubes.split(" ")
                if res[1] == "red" and r < int(res[0]):
                    r = int(res[0])
                elif res[1] == "green" and g < int(res[0]):
                    g = int(res[0])
                elif res[1] == "blue" and b < int(res[0]):
                    b = int(res[0])
                
        result += (r*g*b)
        
    print(result)
