import random

macierz = [[], [], [], []]
for x in range(4):
    for y in range(4):
        macierz[x] = [
            random.randint(0, 10),
            random.randint(0, 10),
            random.randint(0, 10),
            random.randint(0, 10),
        ]

przekatna = [macierz[index_x][index_x] for index_x, x in enumerate(macierz)]