import random as r

def rec(card):
    if stuff[card]!=0:
        return card
    else:
        return r.randint(1,12)

stuff={i:4 for i in range(1,13)}
faces=['Jack','Queen','King']
'''
for i in range(len(faces)):
    stuff[faces[i]]=4
'''
print(stuff)

cards=[r.randint(1,12) for i in range(10)]
print(cards)

def dictCheck():
    for card in cards:
        if all(x==0 for x in stuff.values())==True:
            print("Sorry")
            break
        if stuff[card]==0:
            rec(card)
        stuff[card]-=1

print(stuff)


        
