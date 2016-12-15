cards=[i for i in range(1,10)]
import random as r
'''
def lottery():
    for i in range(5):
        yield random.randint(1,40)
        
lot=lottery()

for i in range(5):
    print(next(lot))

for i in range(5):
    print(random.randint(1,40))

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
'''
def rec(card): #Recursive function to find a card which is in the deck
    if deck[card]>0:
        return card
    else:
        return r.randint(1,13)

def decking(cards):
    for card in cards:
        #print(card)
        if all(x==0 for x in deck.values())==True:
            print("Deck is empty")
            quit()
            break
        elif deck[card]==0:
            rec(card)
        if card>10:
            deck[card][2]-=1
        else:
            deck[card]-=1

def hit(cardss):
    if len(cards)<4:
        cardss.append(r.randint(1,13))
    else:
        cardss[len(cardss)-1]=r.randint(1,13)
        
    decking(cardss)

deck={i:4 for i in range(1,13)}
faces=['Jack','Queen','King']
for i in range(11,14):
    deck[i]=[faces[i-11],10,4]
    
while True:
    hit(cards)
    input("> ")
    if all(x<0 for x in deck.values())==True:
        break
    print(cards)
    print(deck)
