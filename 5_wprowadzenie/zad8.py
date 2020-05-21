from operator import index


class Samogloski:
    """Iterator zwracający tylko samogłoski."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        samogloski = ['a', 'e', 'i', 'o', 'u', 'y', ]
        for litera in self.data:
            if litera.lower() in samogloski:
                self.index = self.data.index(litera)
                self.data = self.data[self.index + 1:]
                return litera


napis = 'Ania lubi jeść placki'
it = Samogloski(napis)
print('{}{}{}{}{}'.format(next(it), next(it), next(it), next(it), next(it)))