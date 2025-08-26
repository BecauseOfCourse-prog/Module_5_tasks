import itertools

deck = []
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
for i in range(13):
    for a in range(4):
        deck.append(cards[i]+" of "+suits[a])

with open('cards.txt', 'w') as cardsFile:
    for cardsCombo in itertools.combinations(deck, 3):
        cardsFile.write("\n" + ", ".join(cardsCombo))