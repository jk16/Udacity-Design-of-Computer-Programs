def poker(hands):
    """Return the best hand: poker[hand,...] => hand"""
    return max(hands, key=hand_rank)

def hand_rank(hand):
    """
    * Nine different kinds of kinds
    * Rankings:
        * Straight flush jack high: (rank=8, high card=11)
        * Four Aces, Queen Kicker: (rank=7, fk = 14, kicker = 12)
        * Full House, Eights over Kings: (rank=6, three = 8, double = 13)
        * Flush, 10-8 (would need all cards to determine tie breaker):
            (rank=5, [])
        * Straight Jack High: (rank=4, 11)
        * Three sevens: (rank=3, three = 7, [])
        * Two Pair-Jacks/Threes: 
            (rank=2, hi of two pair=11, low of two pair=3, [])
        * Pair of Twos, Jack Hi: (rank=1, pair of twos = 2, [])
        * Nothing: (rank=0, [])
    """
    ranks = card_ranks(hand)

    #check to see if we have a sf
    if straight(ranks) and flush(hand):
        high_card = max(ranks)
        rank = 8
        return (rank, high_card)
    elif kind(4, ranks):
        rank = 7
        four_kind = kind(4, ranks)
        kicker = kind(1, ranks)
        return (rank, four_kind, kicker)
    elif kind(3, ranks) and kind(2, ranks):
        rank = 6
        three = kind(3, ranks)
        double = kind(2, ranks)
        return (rank, three, double)
    elif flush(hand):
        rank = 5
        return (rank, hand)
    elif straight(ranks):
        rank = 4
        hi = max(ranks)
        return (rank, hi)
    elif kind(3, ranks):
        rank = 3
        three = kind(3, ranks)
        return (rank, three, hand_rank)
    elif two_pair(ranks):
        rank = 2
        p = two_pair(ranks)
        return (rank, p, hand)
    elif kind(2, ranks):
        rank = 1
        d = kind(2, ranks)
        return (rank, d, ranks)
    else:
        return (0, hand)


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    # using list comprehension:
    
    # ranks = [r for r, s in cards]
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks

def straight(ranks):
    "Return true if the ordered ranks form a 5-card straight."
    high = max(ranks)
    low = min(ranks)
    is_a_flush = (high - low) == 4
    all_cards_different = len(set(ranks)) == 5
    return is_a_flush and all_cards_different

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    all_suits_are_same = len(set(suits)) == 1
    return all_suits_are_same


def test():
    """Test cases for the functions in poker program"""


    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    #test straight function
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,8,6,5]) == False
    #test flush
    assert flush(sf) == True
    assert flush(fk) == False
    #test card_ranks:
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf

    #Test ranking of hands
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7 )
    return "tests pass"

print (test())