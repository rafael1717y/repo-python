import sys
import random

def does_something(arg):
    """ Takes one argument and does something based on type.
    If arg is a string, returns arg * 3;
    If arg is a int or a float, returns arg + 10
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        pass


def foo_bar(arg1, arg2, arg3):
    return arg1, arg2, arg3


def bar(*args):
    return 2 + 2


class Treehouse:
    def one(self):
        return 1

    def two(self):
        return 2

alpha, beta, charlie  = foo_bar(
        "a long string",
        "a long string",
         "and other long string")

one = 1
three = 3

print(Treehouse().two())
