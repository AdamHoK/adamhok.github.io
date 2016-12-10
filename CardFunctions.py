import random as r
import tkinter as tk

dealerCards=[r.randint(1,12) for i in range(2)]
cards=[r.randint(1,12) for i in range(2)]
faces=['Jack','King','Queen']
out=tk.Label(text="?")
end=tk.Label(text="?")
finishing1=tk.Label(text="?")
finishing2=tk.Label(text="?")

def isBust(score):
    if score>21:
        return True
    else:
        return False

def printCards(cards):
    end=[]
    global realCards
    realCards=[]
    end.append("Your cards:")
    for card in cards:
        if card>10:
            end.append(faces[12-card])
            realCards.append(10)
        elif card==1:
            end.append("Ace")
            realCards.append(1)
        else:
            end.append(str(card))
            realCards.append(card)
    end.append("Your score:"); end.append(str(sum(realCards)))
    end="\n".join(end)
    out.configure(text=end)
    out.pack()
    if isBust(sum(realCards))==True:
        bust=tk.Label(text="Bust!")
        bust.pack()
        return True

def hit(cards):
    if len(cards)<4:
        cards.append(r.randint(1,12))
    else:
        cards[len(cards)-1]=r.randint(1,12)
    printCards(cards)

def isWin(score,score2):
    
    if score==21:
        end.configure(text="Blackjack! You won")
        end.pack()
    elif score2==21:
        end.configure(text="Blackjack! Dealer won")
        end.pack()
    if score<21 and score2<21:
        if score>score2:
            end.configure(text="You won")
        elif score2>score:
            end.configure(text="Dealer won")

    elif score==score2: end.configure(text="Draw")
    else:
        if score>21: end.configure(text="You Bust")
        if score2>21: end.configure(text="Dealer Busts")
        else: end.configure(text="this message shouldn't ever appear")
        
    end.pack()
    finishing1.configure(text=("Your cards:",str(sum(cards))))
    finishing2.configure(text=("Dealer's cards:",str(sum(dealerCards))))
    finishing1.pack(); finishing2.pack()
