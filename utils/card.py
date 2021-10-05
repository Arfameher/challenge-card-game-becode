import  typing
# Parent Class
class Symbol:
    """
    Class defining the color and icon of the card.
    """

    def __init__(self, icon: str):       
        
        self.icon = icon
        if self.icon == '♥' or self.icon == '♦':
            color = "Red"
        else:
            color = "Black"
        self.color = color

        # icon = "♥, ♦, ♣, ♠"

    def __str__(self):
        return f"{self.color} {self.icon} "

# Child Class
class Card(Symbol):
    """
    Class defining the value of the card.
    """
    # value = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K"
    
    def __init__(self, value: str, icon: str):
        super().__init__(icon)
        self.value = value
        

    def __str__(self):
        return f"{self.color} {self.value} {self.icon} "

#card = Card("5", "♥") 
#print(card)

