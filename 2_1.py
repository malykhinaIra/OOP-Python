class Product:
    """Class describes a product of online store."""
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise ValueError("Price has to be a number")
        if price <= 0:
            raise ValueError("Price must be > 0")
        self.__price = price

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, int):
            raise ValueError("Dimensions must be an integer number")
        if dimensions <= 0:
            raise ValueError("Dimensions must be > 0")
        self.__dimensions = dimensions

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Invalid type of description")
        if not description:
            raise ValueError("Invalid description")
        self.__description = description


class Customer:
    """Class describes a customer"""
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.phone}'

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Invalid type of surname")
        if any(map(str.isdigit, surname)):
            raise ValueError("Invalid surname")
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid type of name")
        if any(map(str.isdigit, name)):
            raise ValueError("Invalid name")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Invalid type of patronymic")
        if any(map(str.isdigit, patronymic)):
            raise ValueError("Invalid patronymic")
        self.__patronymic = patronymic

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Invalid type of phone")
        self.__phone = phone


class Order:
    """ Class describes an order."""
    def __init__(self, customer):
        self.products = []
        if not isinstance(customer, Customer):
            raise TypeError("Invalid type of customer")
        self.customer = customer

    def __str__(self):
        return f'Total price: {self.total_price}'

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

    @property
    def total_price(self):
        """Returns total price of each order"""
        tmp = 0
        for product in self.products:
            tmp += product.price
        return tmp


p1 = Product(300, 'shirt', 40)
p2 = Product(700, 'jeans', 40)
p3 = Product(250, 'hat', 20)
p4 = Product(80, 'socks', 38)
p5 = Product(300, 'jeans', 42)
c1 = Customer('Malykhina', 'Iryna', 'Olehivna', '0680602271')
order = Order(c1)
order.add_product(p1)
order.add_product(p2)
order.add_product(p3)
order.remove_product(p2)
print(order.customer)
print(order)


