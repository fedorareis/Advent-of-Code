import sys

seeds = []
seed2soil = []
soil2fert = []
fert2water = []
water2light = []
light2temp = []
temp2humid = []
humid2loc = []

def process(file):
    global seeds
    global seed2soil
    global soil2fert
    global fert2water
    global water2light
    global light2temp
    global temp2humid
    global humid2loc
    s2s = False
    s2f = False
    f2w = False
    w2l = False
    l2t = False
    t2h = False
    h2l = False
    for line in file:
        line = line.strip()
        temp = line.split(":")
        if len(temp) == 2: 
            if temp[0] == "seeds":
                seeds = [int(x) for x in temp[1].strip().split(" ")]
            else:
                temp = temp[0].split(" ")
                if temp[0] == "seed-to-soil":
                    s2s = True
                elif temp[0] == "soil-to-fertilizer":
                    s2f = True
                elif temp[0] == "fertilizer-to-water":
                    f2w = True
                elif temp[0] == "water-to-light":
                    w2l = True
                elif temp[0] == "light-to-temperature":
                    l2t = True
                elif temp[0] == "temperature-to-humidity":
                    t2h = True
                elif temp[0] == "humidity-to-location":
                    h2l = True
        elif line == "":
            s2s = False
            s2f = False
            f2w = False
            w2l = False
            l2t = False
            t2h = False
            h2l = False
        else:
            temp = [int(x) for x in line.split(" ")]
            if s2s:
                seed2soil = populate(seed2soil, temp[0], temp[1], temp[2])
            elif s2f:
                soil2fert = populate(soil2fert, temp[0], temp[1], temp[2])
            elif f2w:
                fert2water = populate(fert2water, temp[0], temp[1], temp[2])
            elif w2l:
                water2light = populate(water2light, temp[0], temp[1], temp[2])
            elif l2t:
                light2temp = populate(light2temp, temp[0], temp[1], temp[2])
            elif t2h:
                temp2humid = populate(temp2humid, temp[0], temp[1], temp[2])
            elif h2l:
                humid2loc = populate(humid2loc, temp[0], temp[1], temp[2])


def populate(table, dest, src, len):
    len = len - 1
    # while len >= 0:
    #     table[src + len] = dest + len
    #     len -= 1
    # return table
    mapping = {
        "start": src,
        "end": src + len,
        "dest": dest
    }
    table.append(mapping)
    return table

def convert(table, val):
    for mapping in table:
        if val >= mapping["start"] and val <= mapping["end"]:
            return mapping["dest"] + (val - mapping["start"])
    return val


with open('./input.txt') as f:
    result = sys.maxsize

    process(f)

    for val in seeds:
        s2s = convert(seed2soil ,val)
        # if val in seed2soil:
        #     s2s = seed2soil[val]
        s2f = convert(soil2fert ,s2s)
        # if s2s in soil2fert:
        #     s2f = soil2fert[s2s]
        f2w = convert(fert2water ,s2f)
        # if s2f in fert2water:
        #     f2w = fert2water[s2f]
        w2l = convert(water2light ,f2w)
        # if f2w in water2light:
        #     w2l = water2light[f2w]
        l2t = convert(light2temp ,w2l)
        # if w2l in light2temp:
        #     l2t = light2temp[w2l]
        t2h = convert(temp2humid ,l2t)
        # if l2t in temp2humid:
        #     t2h = temp2humid[l2t]
        h2l = convert(humid2loc ,t2h)
        # if t2h in humid2loc:
        #     h2l = humid2loc[t2h]
        
        if h2l < result:
            result = h2l
        # print(val, s2s,s2f,f2w,w2l,l2t,t2h,h2l)

    # print(seeds)
    # print()
    # print(seed2soil)
    # print()
    # print(soil2fert)
    # print()
    # print(fert2water)
    # print()
    # print(water2light)
    # print()
    # print(light2temp)
    # print()
    # print(temp2humid)
    # print()
    # print(humid2loc)
    # print()
    print(result)