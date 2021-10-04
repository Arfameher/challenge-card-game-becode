import Card from card.py
import random, itertools

class Player:

    def __init__(self, name, cards, turn_count, number_of_cards, history):
        turn_count = 0
        number_of_cards = 0
        self.history = []
        self.name = name
        self.cards = cards
        

    def play(self):
        card = random.shuffle(cards)
        self.history += [card]
        

    def __str__(self):



class Deck():

    def __init__(self, cards):
        self.cards = []

    def fill_deck(self):
        cards = list(itertools.product(icon,value))

    def shuffle(self):
        deck = random.shuffle(cards)

    def distribute(self,player):

    def __str__(self):


