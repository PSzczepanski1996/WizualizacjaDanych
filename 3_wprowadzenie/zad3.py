produkty = {
    'ziemniaki': 'kg',
    'chleb': 'kg',
    'lody': 'sztuki',
    'napoje': 'sztuki',
}

produkty_sztuki = [
    {produkt: wartosc} for produkt, wartosc in produkty.items() if wartosc == 'sztuki'
]
print(produkty_sztuki)