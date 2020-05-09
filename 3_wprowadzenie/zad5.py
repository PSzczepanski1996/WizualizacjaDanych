def zbadaj_funkcje(a1, b1, a2, b2):
    if a1 is a2:
        return 'Są równoległe'
    elif a1 * a2 == -1:
        return 'Są prostopadłe'
    else:
        return 'Brak wyniku'


a1 = int(input('Podaj a1 (y=ax+b): '))
b1 = int(input('Podaj b1 (y=ax+b): '))
a2 = int(input('Podaj a2 (y=ax+b): '))
b2 = int(input('Podaj b2 (y=ax+b): '))
print(zbadaj_funkcje(a1, b1, a2, b2))