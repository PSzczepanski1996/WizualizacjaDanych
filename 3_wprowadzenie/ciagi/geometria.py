def nty_wyraz_geo(a1, n, q):
    return a1*(pow(q, n-1))


def sum_wyrazow_geo(a1, q, n):
    return a1*(1-pow(q, n)/(1-q))
