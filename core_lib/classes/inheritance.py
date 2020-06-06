
class Product:
    _name = 'base'
    _price = 0.0

    @property
    def price(self):
        return int(self._price)

    @price.setter
    def price(self, val):
        self._price = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def display(self):
        print(f'Product: {self.name} is worth {self.price}')


class Soap(Product):
    _name = 'soap'

    def display(self):
        print(f'Soap is of worth {self.price}')


if __name__ == '__main__':
    s = Soap()
    print(s.display())