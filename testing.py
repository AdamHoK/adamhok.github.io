import random as r
import tkinter as tk

dealerCards=[r.randint(1,12) for i in range(2)]+[[]]
cards=[r.randint(1,12) for i in range(2)]+[[]]

sumCards=[]
sumDealer=[]

faces=['Jack','King','Queen']
out=tk.Label(text="?")

def printCards(cards):
    end=[]
    
    
    end.append("Your cards:")
    for card in cards[0:len(cards)-1]:
        print(card)
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

printCards(cards)
print(cards)
