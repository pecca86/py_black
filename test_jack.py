from card import Card
from deck import Deck


#hand value
def count_value(myhand):
    hand_value = 0
    for card in myhand:
        hand_value += card.rank
    return hand_value

#prints all card + values
def print_card_value(myhand):
    for card in myhand:
        print(card, card.rank)
    print("--------")

#changes card value if hand_value is over 10
def check_value(myhand):
    if hand_value > 10:
        for card in myhand:
            if card.rank == 11:
                card.rank = 1
                break
            else:
                print("no card over 5")
                global aces_high 
                aces_high = True



#--------------
mydeck = Deck()
aces_high = False

myhand = []
for i in range(0,5):
    myhand.append(mydeck.play_deck[i])

print_card_value(myhand)
hand_value = count_value(myhand)
print(hand_value)

while hand_value > 10:
    check_value(myhand)
    hand_value = count_value(myhand)
    if aces_high:
        break

print_card_value(myhand)
print(hand_value)