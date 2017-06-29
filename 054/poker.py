import time
from collections import Counter
from enum import IntEnum, unique
start = time.time()

poker_file = open("poker_hands.txt")
hands = str(poker_file.read()).split("\n")
del hands[-1] #deletes empty list item

#Describes numerical rank for the quality of a hand
class Value(IntEnum):
    royal_flush = 10
    straight_flush = 9
    four_kind = 8
    full_house = 7
    flush = 6
    straight = 5
    three_kind = 4
    two_pair = 3
    pair = 2
    high_card = 1


def rank(hand):
    ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
    flush = len(set(suit for _, suit in hand)) == 1
    straight = ranks == list(range(ranks[0], ranks[0] + 5))
    tally = Counter(ranks)
    tallies = sorted(tally.values())

    if straight and flush and ranks[-1] == 14:
        v = Value.royal_flush
    if straight and flush:
        v = Value.straight_flush
    if tallies == [1,4]:
        v = Value.four_kind
    if tallies == [2,3]:
        v = Value.full_house
    if flush and not straight:
        v = Value.flush
    if straight and not flush:
        v = Value.straight
    if tallies == [1,1,3]:
        v = Value.three_kind
    if tallies == [1,2,2]:
        v = Value.two_pair
    if tallies == [1,1,1,2]:
        v = Value.pair
    if tallies == [1,1,1,1,1]:
        v = Value.high_card

    return v



for hand in hands:
    hand = hand.split(' ')
    p1_hand = hand[:5]
    p2_hand = hand[5:]
    print(rank(p1_hand))
