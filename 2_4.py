class BinaryTree:
    """"Binary tree class that contains background information of product prices"""
    def __init__(self, code, price):
        if not isinstance(code, int):
            raise TypeError("Code must be int value")
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Price must be int or float value")
        if price <= 0 or code <= 0:
            raise ValueError("Price and code must be more than 0")
        self.left = None
        self.right = None
        self.code = code
        self.price = price
        self.total_price = 0

    def __str__(self):
        return f'Total price: {self.total_price}'

    def add(self, code, price):
        """"Adds element to the binary tree."""
        if code == self.code:
            raise ValueError("Such code already exists")
        if code < self.code:
            if self.left is None:
                self.left = BinaryTree(code, price)
            else:
                self.left.add(code, price)
        elif code > self.code:
            if self.right is None:
                self.right = BinaryTree(code, price)
            else:
                self.right.add(code, price)

    def search_price(self, code):
        """"Returns price due to product's code."""
        if code < self.code:
            if self.left is None:
                raise ValueError("There is no such product code")
            return self.left.search_price(code)
        if code > self.code:
            if self.right is None:
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
try:
    product_code = int(input("Product code: "))
    quantity = int(input("Quantity: "))
except:
    raise TypeError("Product code and quantity must be int values")

a.get_total_price(product_code, quantity)
print(a)
