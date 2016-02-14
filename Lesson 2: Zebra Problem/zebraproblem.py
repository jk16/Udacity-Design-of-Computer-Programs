import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def imright(h1, h2):
    """
    Storing houses as numbers so if h1 is to the right of h2
    their difference is 1.
    """
    return (h1-h2) == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1# Your code here.


def zebra_puzzle():
    houses = first, _, middle, _ , _ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory)
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
            if Englishman is red
            if Norwegian is first
            if nextto(Norwegian, blue)
            for (coffee, tea, milk, oj, WATER) in orderings
            if coffee is green
            if Ukranian is tea
            if milk is middle
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Kools is yellow
            if LuckyStrike is oj
            if Japanese is Parliaments
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard is dog
            if OldGold is snails
            if nextto(Chesterfields, fox)
            if nextto(Kools, horse)
            )
print (zebra_puzzle())