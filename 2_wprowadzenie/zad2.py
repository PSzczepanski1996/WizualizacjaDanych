import sys

wartosci = [None, None]
print('Podaj dwie wartości')
for index, wartosc in enumerate(wartosci):
    wartosci[index] = int(sys.stdin.readline())
sys.stdout.write(str(wartosci[0] * wartosci[1]))
