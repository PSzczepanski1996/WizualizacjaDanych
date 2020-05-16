def nty_wyraz_aryt(a1, n, r):
    return a1+(n-1)*r


def sum_wyrazow_aryt(a1, n, r):
    an = nty_wyraz_aryt(a1, n, r)
    return ((a1+an)/2)*n
