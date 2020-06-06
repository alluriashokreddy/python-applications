import abc


class AbstractProduct(metaclass=abc.ABCMeta):
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

    @abc.abstractmethod
    def display(self):
        pass


class Soap(AbstractProduct):
    _name = 'soap'
    _price = 50

    def display(self):
        print(f'Soap is of worth {self.price}')


if __name__ == '__main__':
    # This throws an error
    product = AbstractProduct()
    print(product.price)

    # product = Soap()
    # print(product.price)