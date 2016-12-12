faces=['Jack','Queen','King']
deck={i:4 for i in range(1,6)}
for i in range(11,14):
    deck[i]=[faces[i-11],10,4]
sum(deck.values())
