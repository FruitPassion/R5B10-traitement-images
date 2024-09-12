from math import log10

def getSNR(Psignal, Pbruit):
    return 10 * log10(Psignal / Pbruit)

