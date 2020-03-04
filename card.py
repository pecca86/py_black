'''
Card class
'''
class Card():
    suit = ""
    value = ""
    rank = 0

    def __init__(self, suit, value, rank):
        '''
        DOCSTRING: takes in suit, value and rank
        '''
        self.suit = suit
        self.value = value
        self. rank = rank

    def __str__(self):
        '''
        returns this string if object is inside a print statement
        '''
        return f'|{self.value}{self.suit}|'

        