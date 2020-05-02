print('Podaj trzy liczby - a, b, c')
a = int(input())
b = int(input())
c = int(input())

if 0 < a <= 10 and (a>b or b>c):
    print('Warunki są spełnione')
else:
    print('Warunki nie są spełnione')