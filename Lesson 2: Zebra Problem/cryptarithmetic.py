import string, re
import itertools

def solve(formula):
    """
    Given formula of the form: 'ODD + ODD == EVEN', fill in digits
    to solve it.

    output: digit-filled string or None
    """
    for f in fill_in(formula):
        if valid(f):
            print (f)

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]',formula)))
    for digits in  itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters,''.join(digits))
        yield formula.translate(table)

def valid(f):
    "f is valid iff it has no numbers with leading zero, and evals true."
    try:
        return not re.search(r'\b0[0-9]',f) and eval(f) is True
    except ArithmeticError:
        return False



print(solve('ODD + ODD == EVEN'))






















