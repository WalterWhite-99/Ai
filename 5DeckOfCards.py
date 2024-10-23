import itertools,random

cards = ["Spade","Club","Heart","Diamond"]
deck = list(itertools.product(range(1,14),cards))

random.shuffle(deck)

n = int(input("Enter number of Cards to Display: "))

if n > 52:
    print("A deck of cards has only 52 unique cards,try below 52")
else:
    for i in range(n):
        print(deck[i][0], " of " , deck[i][1])
