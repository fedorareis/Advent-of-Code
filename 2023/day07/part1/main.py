from functools import cmp_to_key

five = []
four = []
full = []
three = []
pair2 = []
pair = []
high = []

card = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

def compare(item1, item2):
    hand1 = item1[0]
    hand2 = item2[0]
    i = 0
    while i < len(hand1):
        if card[hand1[i]] < card[hand2[i]]:
            return -1
        elif card[hand1[i]] > card[hand2[i]]:
            return 1
        i += 1

def process(item):
    hand = item[0]
    cards = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }

    trip = False
    dub = False

    for card in hand:
        cards[card] += 1
    
    for k, v in cards.items():
        if v == 5:
            five.append(item)
            return
        if v == 4:
            four.append(item)
            return
        if v == 3:
            if dub:
                full.append(item)
                return
            else:
                trip = True
        if v == 2:
            if dub:
                pair2.append(item)
                return
            elif trip:
                full.append(item)
                return
            else:
                dub = True
    
    if trip:
        three.append(item)
        return
    elif dub:
        pair.append(item)
        return
    else:
        high.append(item)

def score(group, rank):
    total = 0
    group.sort(key=cmp_to_key(compare))
    for item in group:
        total += (int(item[1]) * rank)
        rank += 1
    
    return rank, total

with open('./input.txt') as f:
    result = 0
    rank = 1

    for line in f:
        line = line.strip()
        temp = line.split(" ")
        process(temp)
    
    rank, total = score(high, rank)
    result += total
    rank, total = score(pair, rank)
    result += total
    rank, total = score(pair2, rank)
    result += total
    rank, total = score(three, rank)
    result += total
    rank, total = score(full, rank)
    result += total
    rank, total = score(four, rank)
    result += total
    rank, total = score(five, rank)
    result += total

    print(result)
