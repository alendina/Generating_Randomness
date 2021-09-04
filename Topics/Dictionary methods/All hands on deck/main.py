deck = {str(x): x for x in range(2, 11)}
deck.update(Jack=11, Queen=12, King=13, Ace=14)
rank = [deck[input()] for _ in range(6)]
print(sum(rank) / 6)
