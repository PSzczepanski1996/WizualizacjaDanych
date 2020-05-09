def zbadaj_funkcje(a, b):
    if a > 0:
        return 'Funkcja rosnąca'
    elif not a:
        return 'Funkcja stała'
    else:
        return 'Funkcja malejąca'


a = int(input('Podaj a (y=ax+b): '))
b = int(input('Podaj b (y=ax+b): '))
print(zbadaj_funkcje(a, b))