import  typing
# Parent Class
class Symbol:
    """
    Class defining the color and icon of the card.
    Using the icon, the variable color is set to respective color.
    ♦ ♥ --> Red 
    ♣ ♠ --> Black
    """

    def __init__(self, icon: str):       
        
        # icon = "♥, ♦, ♣, ♠"
        self.icon = icon
        if self.icon == '♥' or self.icon == '♦':
            color = "Red"
        else:
            color = "Black"
        self.color = color

    def __str__(self):
        return f"{self.color} {self.icon} "

# Child Class
class Card(Symbol):
    """
    Class defining the value of the card.
    The values can range in A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
    """
    
    # value = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K"
    def __init__(self, value: str, icon: str):
        super().__init__(icon)
        self.value = value
        

    def __str__(self):
        if self.color == "Red":
            return f" {self.value} \033[1;31m{self.icon}\033[0m " # To print the symbol in colour Red.
        else:
            return f" {self.value} {self.icon} "