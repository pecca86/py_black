'''
test class
'''

import unittest
from card import Card
class TestBJ(unittest.TestCase):

    def test_ace_value(self):
        card1 = Card("D", "11", 11)
        card2 = Card("H", "11", 11)
        card3 = Card("S", "11", 11)
        card4 = Card("C", "11", 11)

        hand = []

        hand.append(card1)
        hand.append(card2)
        hand.append(card3)
        hand.append(card4)
        print(hand)

        self.assertEqual(print(hand), 'D 11 11')


if __name__ == '__main__':
    unittest.main()