cards = {}

def preprocess(file):
    queue = []
    for line in file:
        line = line.strip()
        score = 0
        temp = line.split(": ")
        card = int(temp[0].split(" ")[-1:][0])
        temp = temp[1].split(" | ")
        winning = {}
        for val in temp[0].split(" "):
            if val != "":
                winning[val] = True
        
        for val in temp[1].split(" "):
            if val != "" and val in winning:
                score += 1
        cards[card] = {
            "score": score,
            "count": 1,
        }
        queue.append(card)
    return queue

with open('./input.txt') as f:
    result = 0
    queue = preprocess(f)
    while len(queue) > 0:
        card = queue.pop(0)
        score = cards[card]["score"]
        count = cards[card]["count"]
        while score > 0:
            cards[card+score]["count"] += count
            score -= 1
    
    for k, v in cards.items():
        result += v["count"]

    print(result)
