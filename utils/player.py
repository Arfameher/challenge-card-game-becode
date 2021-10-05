from card import *
import random
from typing import List
import typing

class Player:

    def __init__(self, name):
        self.history = []
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0

    def play(self):
        number = int(input(f"\n{self.name}, you have {len(self.cards)} cards left, choose the card to be played : "))
        card = self.cards[number]
        self.history += [card]
        print(f"{self.name} Turn:{self.turn_count} played : {card.value} {card.icon}")
        return card 

    def __str__(self):
        return f"Name: {self.name} Turn counts: {self.turn_count} Number of Cards: {self.number_of_cards} Cards played: {self.history}"


class Deck():

    def __init__(self):
        self.cards = []  # cards contains LIST OF INSTANCES OF "Card"

    def fill_deck(self):
        icon = "♥, ♦, ♣, ♠".split()
        value = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K".split()
        for i in icon:
            for j in value:
               deck = Card(i,j)  
               self.cards.append(deck)   # cards should contain "52 cards at the end"

        #  self.cards = list(itertools.product(icon,value))

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, players):
        x = 52 // len(players)
        rem = 52 % len(players)
        for player in players:
            for i in range(0,x):
                player.cards.append(self.cards[0])
                self.cards.remove(self.cards[0])

        print("Cards remaining after distributing : ",end = "")
        if rem != 0:
            for i in range(0,rem):
                print(self.cards[0],end = " ")
                self.cards.remove(self.cards[0])
        else:
            print("None.")

    def __str__(self):
        return f"Cards in hand: {self.cards}"


