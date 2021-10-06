class Product:
    def __init__(self,  price, description, dimensions):
        if not isinstance(price, int) or isinstance(price, float):
            raise ValueError("Price has to be a number")
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    def __init__(self,  surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def get_customer_data(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.phone}'


class Order(Product, Customer):
    total_price = 0

    def __init__(self, surname, name, patronymic, phone):
        Customer.__init__(self, surname, name, patronymic, phone)

    def buy(self, price, description, dimensions):
        Product.__init__(self, price, description, dimensions)
        self.total_price += price

    def get_price(self):
        return self.total_price


a = Order('Malykhina', 'Iryna', 'Olehivna', '+380680602271')
a.buy(350, 'shirt', 40)
a.buy(50, 'socks', 39)
a.buy(300, 'hat', 25)
print(a.get_customer_data())
print('Total price:', a.get_price())

b = Order('Melnyk', 'Oksana', 'Romanivna', '+380974673721')
b.buy(1800, 'jacket', 46)
b.buy(300, 'hat', 30)
print(b.get_customer_data())
print('Total price:', b.get_price())



