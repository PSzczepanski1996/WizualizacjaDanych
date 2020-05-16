def lista_zakupow(**rzeczy):
    return sum(rzeczy.values())


produkty = {
    'ziemniaki': 1,
    'chleb': 3,
    'lody': 5,
    'napoje': 4,
}

print(lista_zakupow(**produkty))

