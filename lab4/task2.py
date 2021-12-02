class Product:
    def __init__(self, price, quantity, name):
        self.price = price
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f'\n{self.name}, price: {self.price}, quantity: {self.quantity}'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Invalid type of name")
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise ValueError("Invalid type of quantity")
        if quantity < 0:
            raise ValueError("Positive numbers only")
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise ValueError("Invalid type of price")
        if price <= 0:
            raise ValueError("Positive numbers only")
        self.__price = price


class Composition:

    def __init__(self):
        self.goods = []

    def __iadd__(self, product):
        if not isinstance(product, Product):
            raise TypeError
        if product in (good.name for good in self.goods):
            self.goods[self.goods.index(product.name)].quantity += product.quantity
        else:
            self.goods.append(product)
        return self

    def __getitem__(self, other):
        if not isinstance(other, str):
            raise TypeError("Invalid type of product")
        if other not in (good.name for good in self.goods):
            raise ValueError('There is no such item in composition')
        for good in self.goods:
            if other == good.name:
                return good

    def __setitem__(self, key, value):
        if not isinstance(value, Product):
            raise TypeError("Invalid type of product")
        if key not in (good.name for good in self.goods):
            raise KeyError
        self.goods[self.goods.index(key)] = value

    def __mul__(self, other):
        if not isinstance(other, str):
            raise TypeError("Invalid type of product")
        for good in self.goods:
            if good.name == other and good.quantity:
                return f'{other} is in stock'
        return f'{other} is out of stock'

    def __str__(self):
        return f'{self.goods}'


goods = Composition()
goods += Product(20, 10, 'tomato')
goods += Product(20, 1, 'tomato')
goods += Product(30, 12, 'pineapple')
goods += Product(15, 12, 'apple')
goods += Product(15, 12, 'apple')


print(goods * "apple")
print(goods["apple"])
print(goods["tomato"])
