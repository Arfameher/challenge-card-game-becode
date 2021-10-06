import typing
from utils.card import *
from utils.player import *

class Board():
    """
    This is the Board class where the game begins. An attribute called players is a list of Player.
    It also has attributes to keep count of turn, active cards being played in the roung, and the 
    cards played throughout the game. This class has a method called start_game() which starts the 
    game by creating an object for deck class and calling the fill_deck() method, then shuffle() and 
    distribute() method.
    """
    def __init__(self):
        self.players = [] 
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        #self.points = 0

    def start_game(self):
        """
        Starts the game. Asks the user for how many players are playing, and to input the player names.
        After this the deck is filled and shuffled and then distributed among the players. Next the cards
        are shown to each player in his turn and asked to play his turn.
        """

        self.players = []
        print("\033[1m  \033[94m  \033[4mWelcome to WeTakeYourMoney\033[0m")
        print("Game is starting !! ")
        n = int(input("Enter number of Players : "))
        i = 1 
        while i <= n:
            name = str(input("Enter Player {} name : ".format(i)))
            self.players.append(Player(name))
            i += 1

        deck = Deck()  # Object created.
        deck.fill_deck() # Call fill_deck() to fill the deck. By end of this we have 52 cards!
        deck.shuffle()  # To Shuffle the cards.
        deck.distribute(self.players) # Distribute among the players.
        
        x1 = 52 // len(self.players)  # x1 is number of cards each player has.
        for i in range(0, x1):  
            self.active_cards = []
            for j in self.players:  # Each player has x1 cards.
                card = j.play()  # play() method is called from Player class.
                self.active_cards.append(card)
                j.cards.remove(card)  # Once the card is played by player, it is removed from his cards deck.
                j.turn_count += 1
            self.history_cards.extend(self.active_cards) # To add more than one element in a list use extend()
            self.turn_count += 1
            print(f"\n\033[96mRound : {self.turn_count} complete.\033[0m")
        
            print("Cards played this turn: ",end = "")
            print(*self.active_cards, sep = ",")
            winning_card = self.active_cards[0]
            n1 = 0
            for n in range(1, len(self.active_cards)):
                if str(winning_card.value) < str(self.active_cards[n].value):
                    winning_card = self.active_cards[n]
                    n1 = n
            print(f"Winner of this round : {winning_card} played by {self.players[n1]}")
            
            print(f"Number of cards played in the game : {len(self.history_cards)} --> ", end = "")
            print(*self.history_cards, sep = ",")

        print("No cards left !!")  # This is printed when all the cards are played.
        print(f"Game points : ")
        #for player in players:
        #   print(f"{self.name} {player.self.points}")

    def __str__(self) -> str:
        return f"Player: {self.players}, Turn: {self.turn_count}, Cards in hand: {self.active_cards}"
