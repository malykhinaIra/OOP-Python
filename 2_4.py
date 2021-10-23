class BinaryTree:
    """"Binary tree class that contains background information of product prices"""
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.code = code
        self.price = price
        self.total_price = 0

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must be int value")
        if code <= 0 :
            raise ValueError("Code must be more than 0")
        self.__code = code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Price must be int or float value")
        if price <= 0:
            raise ValueError("price must be more than 0")
        self.__price = price

    def __str__(self):
        return f'Total price: {self.total_price}'

    def add(self, code, price):
        """"Adds element to the binary tree."""
        if code == self.code:
            raise ValueError("Such code already exists")
        if code < self.code:
            if not self.left:
                self.left = BinaryTree(code, price)
            else:
                self.left.add(code, price)
        elif code > self.code:
            if not self.right:
                self.right = BinaryTree(code, price)
            else:
                self.right.add(code, price)

    def search_price(self, code):
        """"Returns price due to product's code."""
        if code < self.code:
            if not self.left:
                raise ValueError("There is no such product code")
            return self.left.search_price(code)
        if code > self.code:
            if not self.right:
                raise ValueError("There is no such product code")
            return self.right.search_price(code)
        return self.price

    def get_total_price(self, code, quantity):
        """"Returns total price"""
        self.total_price = self.search_price(code) * quantity
        return self.total_price


a = BinaryTree(1, 100)
a.add(2, 200)
a.add(3, 300)
a.add(4, 400)
a.add(5, 500)
a.add(6, 600)

product_code = int(input("Product code: "))
amount = int(input("Quantity: "))

a.get_total_price(product_code, amount)
print(a)
