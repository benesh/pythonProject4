def approxEpsilone(number):
    if number == 0:
        return 0
    else:
        return approxEpsilone(number - 1) +(1/ factoriel(number))



def factoriel(number):
    if number == 0:
        return 1
    else:
        return factoriel(number - 1) *number
