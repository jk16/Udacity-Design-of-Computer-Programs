def poker(hands):
    """Return the best hand: poker[hand,...] => hand"""
    return max(hands, key=hand_rank)

def hand_rank(hand):
    return ???


def test():
    """Test cases for the functions in poker program"""


    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()

    assert poker([sf, fk, fh]) == sf
    reeturn "tests pass"

print (test())