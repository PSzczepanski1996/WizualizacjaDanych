from math import sqrt

try:
    zmienna = float(input('Podaj liczbe: '))
    print(sqrt(zmienna))
except ValueError:
    print('Niepoprawna wartość!')