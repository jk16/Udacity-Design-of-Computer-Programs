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
            # for (red, green, ivory, yellow, blue) in orderings
            for (red, green, ivory, yellow, blue) in c(orderings)
            if imright(green, ivory)
            # for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
            for (red, green, ivory, yellow, blue) in c(orderings)
            if Englishman is red
            if Norwegian is first
            if nextto(Norwegian, blue)
            for (coffee, tea, milk, oj, WATER) in orderings
            if coffee is green
            if Ukranian is tea
            if milk is middle
            # for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            for (red, green, ivory, yellow, blue) in c(orderings)
            if Kools is yellow
            if LuckyStrike is oj
            if Japanese is Parliaments
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard is dog
            if OldGold is snails
            if nextto(Chesterfields, fox)
            if nextto(Kools, horse)
            )

def instrument_fn(fn,*args):
    c.starts, c.items = 0,0
    result = fn(*args)
    print ("%s got %s with %5d iters over %7d items" % (fn.__name__, result, c.starts, c.items))

def c(sequence):
    """ Generate items in a sequence; keeping count as we go.
        c.starts --> keeps counts as we go
        c.items --> number of items generated
    """
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item
        
import time

def timedcall(fn, *args):
    t0 = time.clock()
    fn()
    res = fn(*args)
    t1 = time.clock()
    return t1-t0, res

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: if n is int do it n times, 
                                  if its a float do it up to n seconds
                                  return: min/avg/max times
    """
    n_is_int = isinstance(n, int)
    if n_is_int:
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times)<n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)

def average(n):
    return sum(n)/float(len(n))


print(timedcalls(3.5,zebra_puzzle) )








