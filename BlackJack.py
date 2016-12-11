import random as r

#ADAM-PC WAS HERE

#From here
def rec(card):
    if deck[card]>0:
        return card
    else:
        return r.randint(1,12)

def decking(cards):
    for card in cards:
        if all(x==0 for x in deck.values())==True:
            print("Sorry")
            break
        elif deck[card]==0:
            rec(card)
        deck[card]-=1

deck={i:4 for i in range(1,13)}
faces=['Jack','Queen','King']
#To here
#Is for the deck
    
dealerCards=[r.randint(1,12) for i in range(2)]
cards=[4,4,4,4]#[r.randint(1,12) for i in range(2)]
decking(cards); decking(dealerCards)

faces=['Jack','King','Queen']
    
def printCards(cards):
    print("\nYour cards:")
    for card in cards:
        if card>10:
            print(faces[12-card],end=",\r")
        elif card==1:
            print("Ace",end=",\r")
        else:
            print(card, end=",\r")
    print("\nYour score:",sum(cards))
    print()

def isBust(score):
    if score>21:
        return True
    else:
        return False

def isWin(score,score2):
    end=""
    if score==21:
        end="\nBlackjack! You won"
        return end
    elif score2==21:
        end="\nBlackjack! Dealer won"
        return end
    if score<21 and score2<21:
        if score>score2:
            end="\nYou won"
        elif score2>score:
            end="\nDealer won"

    elif score==score2: end="\nDraw"
    else:
        if score>21: end=("\nYou Bust") 
        if score2>21: end=("\nDealer Busts")
        else: end="\nthis message shouldn't ever appear"
    return end
    

def hit(cardss):
    if len(cards)<4:
        cardss.append(r.randint(1,12))
    else:
        cardss[len(cardss)-1]=r.randint(1,12)
    decking(cardss)

def line():
    print("\n","-"*30,"\n")
printCards(cards)

while True:
    decision=int(input("\n1. Hit\n2. Stick\n> "))
    if decision==1:
        hit(cards)
        if isBust(sum(cards))==True:
            print("\nYou bust", end="\r"); print(" with",sum(cards))
            break
        else:
            printCards(cards)
    elif decision==2:
        print(isWin(sum(cards), sum(dealerCards))) 
        break
        
    if sum(dealerCards)>=17:
        print("\nDealer Sticks")
        print(isWin(sum(cards),sum(dealerCards))) 
        break
    else:
        hit(dealerCards)
        print("\nDealer Hits")
