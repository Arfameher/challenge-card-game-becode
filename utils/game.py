import typing
from card import *
from player import *


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

        # call fill_deck()
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
            self.history_cards.append(self.active_cards)
            self.turn_count += 1
            print(f"Turn count: {self.turn_count}")
            print(f"Cards played this turn: {self.active_cards}")
            print(f"Number of cards played in the game : {self.history_cards}")

        print("No cards left !!")

    def __str__(self) -> str:
        return f"Player: {self.players}, Turn: {self.turn_count}, Cards in hand: {self.active_cards}"

board = Board()
board.start_game()
        

