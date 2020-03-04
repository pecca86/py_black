from card import Card
from deck import Deck

'''
Player class
'''


class Player():
    hand = []
    name = ""
    hand_value = 0

    def __init__(self):
        self.player_name()

    def show_hand(self):
        for card in self.hand:
            print(card, end = '')
        self.hand_value += card.rank
        print(f'\nHand value: {self.hand_value}')

    def hit(self, card):
        self.hand.append(card)

    def stay(self):
        pass

    def player_name(self):
        name = input("Please enter your name: ")
        self.name = name


