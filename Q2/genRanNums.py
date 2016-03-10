from math import exp
from math import log
from math import factorial


def p(x, u):
    return u * exp(-u,x)

def b(a, mu):
    if (a == 1.0):
        return 0
    return -1.0/mu * log(1-a)

def pois(k,lam):
    return lam**k * exp(-lam) / factorial(k)
