import random


# defines the values that can be rolled by each die
def rolld2():
    return random.randrange(1,3,1)


def rolld4():
    return random.randrange(1, 5, 1)


def rolld6():
    return random.randrange(1, 7, 1)


def rolld8():
    return random.randrange(1, 9, 1)


def rolld10():
    return random.randrange(1, 11, 1)


def rolld12():
    return random.randrange(1, 13, 1)


def rolld20():
    return random.randrange(1, 21, 1)


def rolld100():
    return random.randrange(1, 101, 1)