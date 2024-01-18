import os

directory = 'decks'

cards = {}
 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    with open(f) as file:
        lines = file.readlines()
    
    for line in lines:
        if line in cards:
            cards[line] = cards[line] + 1
        else:
            cards[line] = 1

count = 0
for w in sorted(cards, key=cards.get, reverse=True):
    if count != 0:
        print(w[2:-1], cards[w])
    count = count + 1
    if count > 31:
        break