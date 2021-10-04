# Parent Class
class Symbol:
    """
    Class defining the color and icon of the card.
    """

    def__init__(self, icon: str, color: str):
        self.color = color
        self.icon = icon
        # "♥, ♦, ♣, ♠".split()

    def __str__(self):
        return f"{self.color} {self.icon}"

# Child Class
class Card(Symbol):
    """
    Class defining the value of the card.
    """
    # value = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K".split()
    
    def __init__(self, value):
        self.value = value
        super().__init(color,icon)

    def __str__(self):
        return f"{self.color} {self.icon} {self.value}"
