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

def rec(card):
    if deck[card]>0:
        return card
    else:
        return rec(r.randint(1,10))

deck={i:4 for i in range(1,11)}

j=0
while True:
    j+=1; x=r.randint(1,10)
    input("> ")
    print(x); y=rec(x)
    deck[y]-=1
    print(y);print(deck)
    if all(z<1 for z in deck.values())==True:
        print("Yes",j)
        break
    
