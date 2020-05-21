class Parzyste:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 2
        try:
            return self.data[self.index]
        except IndexError:
            return self.data[-1]


lista = [11, 12, 13, 14, 15, 16, 17, 18, 19]
it = Parzyste(lista)
print(next(it))
print(next(it))
print(next(it))