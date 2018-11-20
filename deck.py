# Import statements go here
"""
You will create a Deck() class in Python. The Deck() class is sketched out for you in deck-assignment.py, where I've also given you lists of ranks and suits.

Save your solution as deck.py.

Remember, your solution must have the following:

an __init__ method that initializes a shuffled deck.
a __repr__ method
a deal() method that returns a single card. This card should no longer be part of the deck.
I've included a __len__ method so that the len() function will work on your deck, allowing you to check the behavior of your deal() method.

Good luck!
"""

from random import random 
from random import shuffle
from random import * 

suits = ["Spades","Diamonds", "Hearts", "Clubs"]
ranks = [str(r) for r in range(2, 11)] + list('JQKA')
suits = list('cdhs')
card = zip(ranks, suits)

class deck:
    def__init___(self. ranks, suits)
         self.ranks = ranks  
         """I don't know where to place the piece of code above due to "unexpected indent error" -__-""""
         self.suits = suits
            if  self.ranks
    def ___repr__(self): # This is what it should return when the class is called upon, in other words "when you want to generate a random card"
        return("The" %s "of" %s) % (self.ranks, self.suits) 
    def deal(self):
    return (card.apepend) # Because we're trying to add the card(the object) into the list 
