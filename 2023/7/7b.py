import os
from enum import Enum
from functools import cmp_to_key

os.chdir('2023/7')

class HandType(Enum):
    FIVE = 7
    FOUR = 6
    FULL = 5
    THREE = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH = 1

class Hand:
    def __init__(self, cards: str, bet: int):
        self.cards = cards
        self.bet = bet
        self.hand_type = get_hand_type(cards)
    
    def __str__(self):
        return self.cards

def compare_hands(hand1: Hand, hand2: Hand):
    if hand1.hand_type == hand2.hand_type:
        # print(f'got equal {hand1.hand_type} for {hand1.cards} and {hand2.cards}')
        for i, c in enumerate(hand1.cards):
            c1 = card_value(c)
            c2 = card_value(hand2.cards[i])
            # print(f'comparing {c1} to {c2}')
            if c1 != c2:
                return c1 - c2
        # compare chars
        # print('equal hands')
        return 0
    else:
        # print(f'returning {hand1.hand_type.value} - {hand2.hand_type.value}')
        return hand1.hand_type.value - hand2.hand_type.value
    

def card_value(c: str) -> int:
    match c:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 1
        case 'T':
            return 10
        case other:
            return int(c)

# J possibilities
# single J
    # highcard becomes pair
    # pair becomes 3
    # two pair becomes full
    # 3 becomes 4 
    # 4 becomse 5
# 2 J
    # pair becomes 3 (JJXYZ -> XXXYZ, XXJYZ -> XXXYZ)
    # two pair becomes 4 (JJXXZ -> XXXXZ, )
    # full becomes 5
# 3 J
    # 3 becomes 4
    # full becomes 5
# 4 J
    # 4 becomes 5
def upgrade_j(cards: str, hand_type: HandType):
    j_count = cards.count('J')
    print(f"found {j_count} J in {cards}")
    match j_count:
        case 1:
            if hand_type == HandType.HIGH:
                return HandType.PAIR
            if hand_type == HandType.PAIR:
                return HandType.THREE
            if hand_type == HandType.TWO_PAIR:
                return HandType.FULL
            if hand_type == HandType.THREE:
                return HandType.FOUR
            if hand_type == HandType.FOUR:
                return HandType.FIVE
        case 2:
            if hand_type == HandType.PAIR:
                return HandType.THREE
            if hand_type == HandType.TWO_PAIR:
                return HandType.FOUR
            if hand_type == HandType.FULL:
                return HandType.FIVE
        case 3:
            if hand_type == HandType.THREE:
                return HandType.FOUR
            if hand_type == HandType.FULL:
                return HandType.FIVE
        case 4:
            if hand_type == HandType.FOUR:
                return HandType.FIVE

    return hand_type

def get_hand_type(hand):
    sorted_hand = [*hand]
    sorted_hand.sort()
    matches = []
    match_count = 1
    compare_idx = 0
    for i, c in enumerate(sorted_hand):
        if i > 0:
            # print(f'comparing {c} to {sorted_hand[compare_idx]}')
            if c == sorted_hand[compare_idx]:
                match_count += 1
            else:
                matches.append(match_count)
                compare_idx = i
                match_count = 1
            # print(f'match count now {match_count} for char {c}')
    matches.append(match_count)

    result_type = HandType.HIGH
    matches = [x for x in matches if x > 1]
    if len(matches) == 1:
        if matches[0] == 5:
            result_type = HandType.FIVE
        elif matches[0] == 4:
            result_type = HandType.FOUR
        elif matches[0] == 3:
            result_type = HandType.THREE
        elif matches[0] == 2:
            result_type = HandType.PAIR
    elif len(matches) == 2:
        if (matches[0] == 2 and matches[1] == 3) or (matches[0] == 3 and matches[1] == 2):
            result_type = HandType.FULL
        elif (matches[0] == 2 and matches[1] == 2):
            result_type = HandType.TWO_PAIR

    print(f'{hand} would have been {result_type}')
    result_type = upgrade_j(cards=hand, hand_type=result_type)
    print(f'{hand} is now {result_type}')
    
    return result_type


def star1(input_file):
    f = open(input_file, "r")
    hands = []
    for line in f:
        # print(line.strip())
        hand = line.strip().split(' ')[0].strip()
        bet = int(line.strip().split(' ')[1].strip())
        hands.append(Hand(cards=hand, bet=bet))
        print(f'hand {hand} has type {get_hand_type(hand)}')
        # print('')


    print("unsorted hands: ")
    print([str(x) for x in hands])
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))
    print("sorted hands: ")
    print([str(x) for x in sorted_hands])

    winnings = 0
    for i, hand in enumerate(sorted_hands):
        winnings += hand.bet * (i+1)
    print(f'winnings {winnings}')

# input = "7-my-test.input"
# input = "7-test.input"
input = "7.input"
star1(input)
