from card import Card
from random import randint
'''
Card deck class for our black jack game
'''

class Deck():
    deck_size = 52
    play_deck = []

    def __init__(self):
        '''
        initiates the deck and creates all the cards for it
        '''
        Deck.addCards(self, '\u2663')   #clubs
        Deck.addCards(self,'\u2665')   #hearts
        Deck.addCards(self,'\u2666')   #diamonds
        Deck.addCards(self,'\u2660')   #spades
        #after the cards have been added, we shuffle the deck
        Deck.shuffle(self)

    def addCards(self, suit):
        '''
        Adds all the cards beloning to the suit given as an argument
        '''
        self.play_deck.append(Card(suit, "Ace", 11))

        for i in range(2,11):
            self.play_deck.append(Card(suit, str(i), i))

        self.play_deck.append(Card(suit, "Jack", 10))
        self.play_deck.append(Card(suit, "Queen", 10))
        self.play_deck.append(Card(suit, "King", 10))

    def print_deck(self):
        '''
        prints out every card in the deck
        '''
        for card in self.play_deck:
            print(card)
    
    def shuffle(self):
        tmp = Card("","",0)

        for i in range(0,400):
            rand1 = randint(0,51)
            rand2 = randint(0,51)

            tmp = self.play_deck[rand1]
            self.play_deck[rand1] = self.play_deck[rand2]
            self.play_deck[rand2] = tmp

    #def deal_card(self):
    def deal_card(self, player):
        dealt_card = self.play_deck.pop()
        return dealt_card

    def __len__(self):
        '''
        returns the value if the object's len is called
        '''
        return self.deck_size


#deck_test = Deck()
#deck_test.print_deck()
