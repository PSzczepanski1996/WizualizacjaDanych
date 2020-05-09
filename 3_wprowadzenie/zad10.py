def lista_zakupow(**rzeczy):
    return len(rzeczy)


produkty = {
    'ziemniaki': 'kg',
    'chleb': 'kg',
    'lody': 'sztuki',
    'napoje': 'sztuki',
}

print(lista_zakupow(**produkty))

