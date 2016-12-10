import tkinter as tk
import random as r
from CardFunctions import printCards, hit, isBust, isWin

output=tk.Label(text="Output Here'")
dealerCards=[r.randint(1,13) for i in range(2)]+[[]]
cards=[r.randint(1,13) for i in range(2)]+[[]]
print(cards,dealerCards)
faces=['Jack','King','Queen']

window=tk.Tk()

pc=tk.Button(text="Your Cards",command=lambda: printCards(cards))
hitt=tk.Button(text="Hit", command=lambda: hit(cards))
stick=tk.Button(text="Stick",command=lambda: isWin(sum(cards),sum(dealerCards)))

if sum(dealerCards[len(dealerCards)-1])>=17:
    output.configure(text="Dealer Sticks")
    isWin(sum(cards),sum(dealerCards))
else:
    hit(dealerCards)
    output.configure(text="Dealer Hits")

pc.pack(side=tk.LEFT)
hitt.pack(side=tk.LEFT)
stick.pack(side=tk.RIGHT)

window.mainloop()
