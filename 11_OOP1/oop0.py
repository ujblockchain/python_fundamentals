"""
Each Python class definition has an implicit superclass: object

The superclass or parent of our user-defined class is the object superclass
"""
from typing import Tuple
# from enum import Enum
# This is the basic format for creating classes
class ClassName:
    pass 

# print the class name of ClassName
print(ClassName.__class__)

# access the base class of ClassName
print(ClassName.__class__.__base__)

"""
Fundamental to the life cycle of an objects are 
- creation
- initialisation
- destruction

"""
# initialisation sets the initial state of the object

class Rectangle:

    def area(self) -> float:
        return self.length * self.width

# Super class
class Card:
    def __init__(self, rank:str, suit:str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11

class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10
"""
The __init__() method is factored into the superclass so that a common initialisation in the superclass.

we see a polymorphic design in the subclasses with the _points method. 

All the subclasses have identical methods and attributes.

Objects of these subclasses can be used interchangeably in a application
"""

# enumration of the class, rank, and suit for several cards in a list
cards = [AceCard('A', '♠'), Card('2','♠'), FaceCard('J','♠'),]
# this method is tedious and error-prone

"""
Creating enumerated constants
Classes for the card suits can be defined - the suits of playing cards have a domain that can be enumerated.

The suit of the playing card should not change once defined - immutable
"""

from enum import Enum
class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"
# here the enumerated values must be qualified by the class name, assuring that there will be no collisions with other objects

print(Suit.Club)

cards = [AceCard('A', Suit.Spade), Card('2', Suit.Spade),
FaceCard('Q', Suit.Spade),]


# Factory function
"""
This is better than enumerating all the 52 cards in a deck.

Common approach to factory functions:
1 - create a function that creates objects of the required class
2 - define a class that has methods for creating objects - FACTORY DESIGN PATTERN
"""

def card(rank:int, suit:Suit) -> Card:
    if rank ==1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11 <= rank <14:
        name = {11: "J", 12:"Q", 13:"K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")

card_deck = []
for suit in list(Suit):
    for rank in range(1,14):
        card_deck.append(card(rank, suit))

print(card_deck[0:20])

def card_new(rank:int, suit:Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif rank == 11:
        return FaceCard("J",suit)
    elif rank == 12:
        return FaceCard("Q",suit)
    elif rank == 13:
        return FaceCard("K",suit)
    else:
        raise Exception("Rank out of range")
    

class CardFactory:
    def rank(self, rank:int) -> "CardFactory":
        self.class_, self.rank_str = {
            1: (AceCard, "A"),
            2: (FaceCard, "J"),
            3: (FaceCard,"Q"),
            4: (FaceCard, "K")
        }.get(
            rank, (Card, str(rank))
        )
        return self
    def suit(self, suit:Suit) -> Card:
        return self.class_(self.rank_str, suit)
    
card_fac = CardFactory()
card_deck_2 = []
for s in Suit:
    for r in range(13):
        new_card = card_fac.rank(r+1).suit(s)
        card_deck_2.append(new_card)

print(card_deck_2)