import random as r
import tkinter as tk

dealerCards=[r.randint(1,13) for i in range(2)]+[[]]

cards=[r.randint(1,13) for i in range(2)]+[[]]


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
    
    
    end.append("Your cards:")
    for card in cards[0:len(cards)-1]:
        if card>10:
            cards[len(cards)-1].append(10)
            end.append(faces[13-card])
        elif card==1:
            end.append("Ace")
            cards[len(cards)-1].append(1)
        else:
            end.append(str(card))
            cards[len(cards)-1].append(card)
    end.append("Your score:"); end.append(str(sum(cards[len(cards)-1])))
    end="\n".join(end)
    out.configure(text=end)
    out.pack()
    if isBust(sum(cards[len(cards)-1]))==True:
        bust=tk.Label(text="Bust!")
        bust.pack()
        return True

def hit(cards):
    if len(cards)<5:
        cards.insert(len(cards)-1,r.randint(1,13))
    else:
        cards[len(cards)-1]=r.randint(1,13)
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
