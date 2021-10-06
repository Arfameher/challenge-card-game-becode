import typing
from utils.card import *
from utils.player import *


class Board():

    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):

        self.players = []
        print("Game is starting !! ")
        n = int(input("Enter number of Players : "))
        i = 1 
        while i <= n:
            name = input("Enter Player {} name : ".format(i))
            self.players.append(Player(name))
            i += 1

        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)
        x1 = 52 // len(self.players)
        for i in range(0, x1):
            self.active_cards = []
            for j in self.players:
                card = j.play()
                self.active_cards.append(card)
                j.cards.remove(card)
                j.turn_count += 1
            self.history_cards.extend(self.active_cards) # To add more than one element in a list use extend()
            self.turn_count += 1
            print(f"Round : {self.turn_count} complete.")
            print("Cards played this turn: ",end = "")
            print(*self.active_cards, sep = ",")
            print(f"Number of cards played in the game : {len(self.history_cards)} --> ", end = "")
            print(*self.history_cards, sep = ",")

        print("No cards left !!")

    def __str__(self) -> str:
        return f"Player: {self.players}, Turn: {self.turn_count}, Cards in hand: {self.active_cards}"
