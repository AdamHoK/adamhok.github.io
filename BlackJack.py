import random as r

dealerCards=[r.randint(1,12) for i in range(2)]
cards=[r.randint(1,12) for i in range(2)]
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
    #print("\nYour score:\n",score,
    #      "\nDealer's score:\n",score2)
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
    

def hit(cards):
    if len(cards)<4:
        cards.append(r.randint(1,12))
    else:
        cards[len(cards)-1]=r.randint(1,12)

def line():
    print("\n","-"*30,"\n")
printCards(cards)

while True:
    decision=int(input("\n1. Hit\n2. Stick\n> "))
    if decision==1:
        hit(cards)
        #print("\nYour score:\n", #HERE
        #      sum(cards),
        #      "\nDealer's score:\n" #HERE
        #      ,sum(dealerCards))
        
        if isBust(sum(cards))==True:
            print("\nYou bust")
            break
        else:
            printCards(cards) #HERE
    elif decision==2:
        print(isWin(sum(cards), sum(dealerCards))) #HERE
        break
        
    if sum(dealerCards)>=17:
        print("\nDealer Sticks")
        print(isWin(sum(cards),sum(dealerCards))) #HERE
        break
    else:
        hit(dealerCards)
        print("\nDealer Hits")#HERE

