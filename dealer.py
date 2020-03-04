'''
Dealer class, automated
'''

class Dealer():
    hand = []
    name = "Dealer"
    hand_value = 0

    def __init__(self):
        pass
    
    def hit(self, card):
        '''
        hits a new card until hand is better than players
        or bust
        '''
        self.hand.append(card)

    def show_hand(self):
        '''
        Shows the players hand
        '''
        for card in self.hand:
            print(card, end = '')
        self.hand_value += card.rank
        print(f'\nHand value: {self.hand_value}')
