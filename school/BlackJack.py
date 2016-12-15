import random as r

#ADAM-PC WAS HERE

def summ(cards):
    #global summer
    summer=[]
    for card in cards:
        if card>10:
            summer.append(10)
        else:
            summer.append(card)
    return sum(summer)

#From here
def rec(card): #Recursive function to find a card which is in the deck
    if deck[card]>0:
        return card
    else:
        return r.randint(1,12)

def decking(cards):
    for card in cards:
        if all(x==0 for x in deck.values())==True:
            print("Deck is empty")
            break
        elif deck[card]==0:
            rec(card)
        if card>10:
            deck[card][2]-=1
        else:
            deck[card]-=1

deck={i:4 for i in range(1,13)}
faces=['Jack','Queen','King']
for i in range(11,14):
    deck[i]=[faces[i-11],10,4]

#To here
#Is for the deck
    
dealerCards=[r.randint(1,12) for i in range(2)]
cards=[r.randint(1,12) for i in range(2)]
decking(cards); decking(dealerCards)



faces=['Jack','King','Queen']
    
def printCards(cards):
    print("Your cards:")
    for card in cards:
        if card>10:
            print(faces[12-card],end=" ")
        elif card==1:
            print("Ace",end=" ")
        else:
            print(card, end=" ")
            
    print("\nYour score:",summ(cards))
    line()

def isBust(score):
    if score>21:
        return True
    else:
        return False

def isWin(score,score2):
    end=""
    if score==21:
        end="\nBlackjack! You won"
        return end, score
    elif score2==21:
        end="\nBlackjack! Dealer won"
        return end, score2
    if score<21 and score2<21:
        if score>score2:
            return "You won", score
        elif score2>score:
            return "\nDealer won", score2 

    elif score==score2: return "\nDraw", 0
    else:
        if score>21: return ("\nYou Bust"), score
        if score2>21: return ("\nDealer Busts"), score2
        else: return "\nthis message shouldn't ever appear", 0
    #return end, score
    

def hit(cardss):
    if len(cards)<4:
        cardss.append(r.randint(1,12))
    else:
        cardss[len(cardss)-1]=r.randint(1,12)
    decking(cardss)

def line():
    print("-"*30)
    
printCards(cards)

while True:
    decision=int(input("1. Hit\n2. Stick\n> "))
    line()
    if decision==1:
        hit(cards)
        if isBust(summ(cards))==True:
            print("You bust", end=""); print(" with",summ(cards))
            line()
            break
        else:
            printCards(cards)
        #line()
    elif decision==2:
        print(isWin(summ(cards), summ(dealerCards))[0],"with",isWin(summ(cards),summ(dealerCards))[1]) 
        line()
        break
        
    if sum(dealerCards)>=17:
        print("Dealer Sticks")
        print(isWin(summ(cards),summ(dealerCards))[0],"with",isWin(summ(cards),summ(dealerCards))[1]) 
        line()
        break
    else:
        hit(dealerCards)
        print("Dealer Hits")

print("Dealer's card were:")
for card in dealerCards:
    if card>10:
        print(faces[12-card],end=" ")
    elif card==1:
        print("Ace",end=" ")
    else:
        print(card, end=" ")
print("\nDealer had a score of:",summ(dealerCards))
