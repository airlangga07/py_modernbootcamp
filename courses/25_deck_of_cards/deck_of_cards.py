class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit  = suit
    
    def __repr__(self):
        return "<Card: {} of {}>".format(self.value, self.suit)


c = Card("A", "hearts")
print(c)
