import time
from enum import IntEnum, unique
start = time.time()

poker_file = open("poker_hands.txt")
hands = str(poker_file.read()).split("\n")
del hands[-1] #deletes empty list item

#Describes numerical rank for the quality of a hand
class Quality(IntEnum):
    high_card = 1
    pair = 2
    two_pair = 3
    three = 4
    straight = 5
    flush = 6
    full_house = 7
    four = 8
    straight_flush = 9
    royal_flush = 10


def rank(hand):
    ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
    flush = len(set(suit for _, suit in hand)) == 1
    straight = ranks == list(range(ranks[0], ranks[0] + 5))
    return ranks



for hand in hands:
    hand = hand.split(' ')
    p1_hand = hand[:5]
    p2_hand = hand[5:]
    print(rank(p1_hand))
