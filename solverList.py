import random




def solverPuzzle(puzzle):
    for i in range(len(puzzle)):
        if isCelEmpty(puzzle[i]):
            puzzle[i] = getRightNumber(puzzle)
    return puzzle


# check if the place is empty meaning minor
def isCelEmpty(i):
    return i < 0


def guesstNumber():
    return random.randint(1, 9)


def getRightNumber(puzzle):
    verif = False
    while verif == False:
        guess = guesstNumber()
        if not ifNumberExist(puzzle, guess):
            verif = True
    return guess


def ifNumberExist(puzzle, number):
    for i in puzzle:
        if i == number:
            return True
    return False
