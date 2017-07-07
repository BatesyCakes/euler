import time
from collections import Counter
from enum import IntEnum, unique
start = time.time()

poker_file = open("poker_hands.txt")
hands = str(poker_file.read()).split("\n")
del hands[-1] #deletes empty list item

#Describes numerical rank for the quality of a hand
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
    '''Provides a numerical rank for cards. Tallies for pairs and
    suits. provides a tie-breaker'''
    ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
    flush = len(set(suit for _, suit in hand)) == 1
    straight = ranks == list(range(ranks[0], ranks[0] + 5))
    tally = Counter(ranks)
    tallies = sorted(tally.values())
    distinct_ranks = sorted(tally, key = lambda v:(tally[v], v), reverse=True)

    if straight and flush and ranks[-1] == 14:
        v = royal_flush
    if straight and flush:
        v = straight_flush
    if tallies == [1,4]:
        v = four_kind
    if tallies == [2,3]:
        v = full_house
    if flush and not straight:
        v = flush
    if straight and not flush:
        v = straight
    if tallies == [1,1,3]:
        v = three_kind
    if tallies == [1,2,2]:
        v = two_pair
    if tallies == [1,1,1,2]:
        v = pair
    if tallies == [1,1,1,1,1]:
        v = high_card
    return v, distinct_ranks


def wins(hands):
    '''Splits each hand into player's hands, calls on ranks function to
    determine hand winner. Tallies p1 wins.'''

    wins = 0
    for hand in hands:
        hand = hand.split(' ')
        p1_hand = hand[:5]
        p2_hand = hand[5:]

        if rank(p1_hand)[0] > rank(p2_hand)[0]:
            wins += 1
        elif rank(p1_hand)[0] < rank(p2_hand)[0]:
            pass
        elif rank(p1_hand)[0] == rank(p2_hand)[0]:
            if rank(p1_hand)[1][0] > rank(p2_hand)[1][0]:
                wins += 1
            else:
                pass
    return wins


print(wins(hands))
