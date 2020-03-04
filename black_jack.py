from deck import Deck
from card import Card
from player import Player
from dealer import Dealer
import time
'''
Class from where we start our black jack game
'''

class BlackJack():
    #attributes
    game_deck = []
    player1 = ""
    dealer = ""
    #evaluating if the game is still on-going
    game_on = True
    aces_high = False

    def __init__(self):
        #creates the game deck
        self.game_deck = Deck()

        #creates the player
        self.player1 = Player()

        #creates the dealer
        self.dealer = Dealer()
        
        #self.deal_card()
        self.deal_card(self.player1)
        #start the game
        self.begin()


    def begin(self):
        '''
        Starts the game.
        '''
        while self.game_on:
            player_action = input("hit or stay?: ")
            if player_action == "hit":
                self.deal_card(self.player1)
                self.evaluate_hand(self.player1)
            elif player_action == "stay":
                #cant use game_on = False, since it quits the whole game
                break
            elif player_action == "quit":
                self.game_on = False
            else:
                print("Allowed commands: hit, stay or quit")
        #when player is happy and not bust, we call the dealer
        self.dealers_turn()

    def deal_card(self, player):
        '''
        DOCSTRING: Deals the cards to the player
        player: either human player or CPU dealer
        '''
        print(f"{player.name}'s turn")
        #calls the Deck class' deal_card method
        dealt_card = self.game_deck.deal_card(player)
        #calls the Player class' hit method
        player.hit(dealt_card)
        #calls the Player class' show_hand method
        player.show_hand()

    def evaluate_hand(self, player):
        '''
        evaluates if player is over or not
        '''
        if player.hand_value == 21:
            print("BLACK JACK!")
            self.dealers_turn()
        if player.hand_value > 21:
            #if hand value is over 21 we check for aces and turn the first
            #occurance of an ace into the value of 1
            self.recount_hand(player)

            if player.hand_value > 21:
                #if the hand value is after the correction still > 21
                print(f"{player.name} bust!!")
                self.game_on = False

            if player.hand_value < 21 and player.name == "Dealer":
                #in case the dealer gets an ace and have o lower hand value
                #than the player
                self.dealers_turn()
    
    def recount_hand(self, player):
        '''
        Checks for aces in the players hand when the hand value is > 21
        '''
        for card in player.hand:
            if card.rank == 11:
                card.rank = 1
                player.hand_value -= 10
                print(f'New hand value: ', end= ' ')
                print(player.hand_value)
            else:
                #True = there were no more aces in the hand of the value of 11
                self.aces_high = True

    
    def dealers_turn(self):
        '''
        DOCSTRING: Dealer class, automated
        '''
        while self.game_on:
            if self.dealer.hand_value < self.player1.hand_value:
                self.deal_card(self.dealer)
                #timer so it prints slower to the console
                time.sleep(1.2)
            elif self.dealer.hand_value > 21:
                self.evaluate_hand(self.dealer)
                print(f'{self.player1.name} WON!')
                self.game_on = False
            elif self.dealer.hand_value >= self.player1.hand_value and self.dealer.hand_value <= 21:
                print("dealer won!")
                self.game_on = False
            else:
                print("dealer won!")
                self.game_on = False


game = BlackJack()

