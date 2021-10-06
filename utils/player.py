import random
import typing
from typing import List
from utils.card import *

class Player:
    """
    A class Player where each players attributes are stored.
    Player's name, the cards the player has in hand, which turn the player is playing,
    and the cards played throughout the game.
    """

    def __init__(self, name):  # Takes the name from the object defined
        self.history = []
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0

    def play(self):
        """ 
        Displays the cards present in players hand, and then takes input from the user to choose
        which card to play. Displays all the relevant information for that round played by the 
        player.
        """

        print("\n")
        print(*self.cards, sep = ',')  # Prints out the cards in hand.
        number = int(input(f"{self.name}, you have {len(self.cards)} cards left, choose the card index number to be played : "))
        card = self.cards[number] # card is set to the card value chosen by the player.
        self.history += [card]
        print(f"{self.name} Round : {self.turn_count} Played Card : {card.value} {card.icon}")
        return card 

    def __str__(self):
        return f"Name: {self.name} Turn counts: {self.turn_count} Number of Cards: {self.number_of_cards} Cards played: {self.history}"


class Deck():
    """
    An attribute cards which contains list of instances of Card.
    It has fill_deck() method to fill the deck with all cards. To shuffle the deck use 
    shuffle() method and then to distribute the cards among the players use distribute() 
    method.
    """

    def __init__(self):
        self.cards = []  # cards contains LIST of INSTANCES of "Card"

    def fill_deck(self):
        """
        This is a method to fill the deck of cards using the icon and value.
        """
        icon = "♥ ♦ ♣ ♠".split()
        value = "A 2 3 4 5 6 7 8 9 10 J Q K".split()
        for i in icon:
            for j in value:
               deck = Card(j,i)  # Passing the VALUE first and then the ICON to the Card class.
               self.cards.append(deck)   # cards should contain "52 cards at the end"

    def shuffle(self):  # Method to shuffle all the cards using random.shuflle
        random.shuffle(self.cards)

    def distribute(self, players):
        """
        Once all the cards are shuffled, they are distributed among all the players.
        Define a variable that stores how many cards are to be divided amongst the players and store
        remaining in another variable called rem.
        """
        x = 52 // len(players)  # x cards to be given to each player.
        rem = 52 % len(players)  # remaining cards after divided among players.
        for player in players:
            for i in range(0,x):
                player.cards.append(self.cards[0])  # Each player gets x cards.
                self.cards.remove(self.cards[0])  # Once the card is given to the player, it must be removed from deck.

        print("Cards remaining after distributing : ",end = "")
        if rem != 0:
            for i in range(0,rem):
                print(self.cards[0],end = " ")  # Printing out the remaining cards in the deck.
                self.cards.remove(self.cards[0])
        else:
            print("None.")
        
    def __str__(self):
        return f"Cards in hand: {self.cards}"


