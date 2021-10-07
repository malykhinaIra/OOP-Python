class Product:
    def __init__(self,  price, description, dimensions):
        if not isinstance(price, int) and not isinstance(price, float):
            raise ValueError("Price has to be a number")
        elif price <= 0 or dimensions <= 0:
            raise ValueError("Positive numbers only")
        else:
            self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    def __init__(self,  surname, name, patronymic, phone):
        if not isinstance(surname, str) or not isinstance(surname, str) or not isinstance(patronymic, str):
            raise TypeError("Invalid type of name, surname or patronymic")
        if any(map(str.isdigit, surname)) or any(map(str.isdigit, name)) or any(map(str.isdigit, patronymic)):
            raise ValueError("Invalid name, surname or patronymic")
        else:
            self.surname = surname
            self.name = name
            self.patronymic = patronymic
        if not isinstance(phone, str) or len(phone) != 10 or any(map(str.isalpha, phone)):
            raise ValueError("Invalid phone number")
        else:
            self.phone = phone

    def get_customer_data(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.phone}'


class Order:
    def __init__(self, customer, *products):
        self.customer = customer
        self.products = products
        self.__total_price = 0
        for product in self.products:
            self.__total_price += product.price

    def get_price(self):
        return self.__total_price


c1 = Customer('Malykhina', 'Iryna', 'Olehivna', '0680602271')
order1 = Order(c1, Product(350, 'shirt', 40), Product(300, 'hat', 25))
print(c1.get_customer_data())
print('Total price:', order1.get_price())

c2 = Customer('Melnyk', 'Oksana', 'Romanivna', '0974673721')
order2 = Order(c1, Product(50, 'socks', 39), Product(300, 'hat', 25), Product(1800, 'jacket', 46))
print(c2.get_customer_data())
print('Total price:', order2.get_price())


