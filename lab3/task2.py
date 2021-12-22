import calendar
import json
import pprint
import random


def unique_id():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


class Customer:
    """Class describes a customer"""

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

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


class Pizza:
    """ Class describes a pizza."""

    def __init__(self, day=""):
        self.name = data[day]["name"]
        self.price = data[day]["price"]
        self.ingredients = data[day]["ingredients"]

    def __repr__(self):
        return f'{self.name, self.ingredients}'

    def add_ingredient(self, *ingredients):
        """ Adds ingredients to pizza and calculates new price."""
        for ingredient in ingredients:
            if ingredient not in data["Ingredients"]:
                raise ValueError("Such ingredient is not available")
            self.ingredients.append(ingredient)
            self.price += data["Ingredients"][ingredient]


class MondayPizza(Pizza):
    def __init__(self):
        super().__init__("Monday")


class TuesdayPizza(Pizza):
    def __init__(self):
        super().__init__("Tuesday")


class WednesdayPizza(Pizza):
    def __init__(self):
        super().__init__("Wednesday")


class ThursdayPizza(Pizza):
    def __init__(self):
        super().__init__("Thursday")


class FridayPizza(Pizza):
    def __init__(self):
        super().__init__("Friday")


class SaturdayPizza(Pizza):
    def __init__(self):
        super().__init__("Saturday")


class SundayPizza(Pizza):
    def __init__(self):
        super().__init__("Sunday")


class Order:
    """ Class describes an order."""

    def __init__(self, customer, date):
        self.id = next(unique_id())
        self.customer = customer
        self.day = date
        self.pizza = Pizza()
        self.pizzas = []

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Invalid type of customer")
        self.__customer = customer

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, date):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day, month, year = (int(x) for x in date.split('/'))
        self.__day = days[calendar.weekday(year, month, day)]

    def __str__(self):
        return f'Order for {self.customer}:\n{len(self.pizzas)} pizza(s)-of-{self.day} ' \
               f'"{self.pizza.name}", total price {self.total_price}\n'

    def buy_pizza_of_the_day(self):
        """Adds appropriate due to day of week pizza to the list"""
        day_pizza_dict = {"Monday": MondayPizza(), "Tuesday": TuesdayPizza(), "Wednesday": WednesdayPizza(),
                          "Thursday": ThursdayPizza(), "Friday": FridayPizza(), "Saturday": SaturdayPizza(),
                          "Sunday": SundayPizza()}
        self.pizza = day_pizza_dict[self.day]

        with open('pizzas.json', 'r') as f:
            pizzas_info = json.load(f)

        self.pizza.ingredients = pizzas_info[self.day]["ingredients"]
        self.pizzas.append(self.pizza)

    @property
    def total_price(self):
        """Returns total price of each order"""
        tmp = 0
        for pizza in self.pizzas:
            tmp += pizza.price
        return tmp


with open('pizzas.json', 'r') as file:
    data = json.load(file)
order1 = Order(Customer('Malykhina', 'Iryna', 'Olehivna'), '12/11/2021')
order1.buy_pizza_of_the_day()

order2 = Order(Customer('Melnyk', 'Oksana', 'Romanivna'), '13/11/2021')
order2.buy_pizza_of_the_day()
order2.buy_pizza_of_the_day()
order2.pizza.add_ingredient("pineapple")
order2.buy_pizza_of_the_day()

print(order1)
print(order2)

orders = {order1.id: order1.__dict__}
orders.update({order2.id: order2.__dict__})
with open('sold_tickets.json', 'a+') as f:
    json.dump(orders, f, indent=4, default=str)

# with open('sold_tickets.json', 'r') as f:
#     pprint.pprint(json.load(f))
