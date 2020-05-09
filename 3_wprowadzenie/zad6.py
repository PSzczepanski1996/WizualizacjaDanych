from math import sqrt


def promien(x=2, a=1, y=2, b=1):
    return sqrt(((x-a)*(x-a))+((y-b)*(y-b)))


print(promien())