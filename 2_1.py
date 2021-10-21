class Product:
    """Class describes a product of online store."""
    def __init__(self, price, description, dimensions):
        if not isinstance(price, int) and not isinstance(price, float):
            raise ValueError("Price has to be a number")
        if not isinstance(dimensions, int):
            raise ValueError("Dimensions have to be integer number")
        if price <= 0 or dimensions <= 0:
            raise ValueError("Positive numbers only")
        if not isinstance(description, str):
            raise ValueError("Invalid type of description")
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    """Class describes a customer"""
    def __init__(self, surname, name, patronymic, phone):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(patronymic, str):
            raise TypeError("Invalid type of name, surname or patronymic")
        if any(map(str.isdigit, surname)) or any(map(str.isdigit, name)) or any(map(str.isdigit, patronymic)):
            raise ValueError("Invalid name, surname or patronymic")
        if not isinstance(phone, str) or any(map(str.isalpha, phone)):
            raise ValueError("Invalid phone number")
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone
        self.order = Order()

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.phone}'


class Order:
    """ Class describes an order."""
    def __init__(self):
        self.products = list()
        self.total_price = 0

    def __str__(self):
        return f'Total price: {self.counting()}'

    def add_product(self, product):
        """Adds product to the list"""
        if not isinstance(product, Product):
            raise TypeError("Invalid type of product")
        self.products.append(product)

    def remove_product(self, product):
        """Removes product from the list"""
        if not isinstance(product, Product):
            raise TypeError("Invalid type of product")
        self.products.remove(product)

    def counting(self):
        """Returns total price of each order"""
        for product in self.products:
            self.total_price += product.price
        result = self.total_price
        self.total_price = 0
        return result


p1 = Product(300, 'shirt', 40)
p2 = Product(700, 'jeans', 40)
p3 = Product(250, 'hat', 20)
p4 = Product(80, 'socks', 38)
p5 = Product(300, 'jeans', 42)

customer = Customer('Malykhina', 'Iryna', 'Olehivna', '0680602271')
print(customer)

customer.order.add_product(p1)
customer.order.add_product(p2)
customer.order.add_product(p3)
print(customer.order)

