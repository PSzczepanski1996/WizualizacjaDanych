zmienna = input('Podaj zmienna: ')
index = 0
suma_cyfr = 0
while zmienna:
    try:
        suma_cyfr += int(zmienna[index])
        index += 1
    except IndexError:
        print(f'Suma cyfr to {suma_cyfr}')

