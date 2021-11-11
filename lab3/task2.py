import json

info = {
    "Ingredients":
        {
            "tomatoes": 15,
            "mozzarella": 30,
            "mushrooms": 25,
            "ham": 15
        },
    "Monday": {
        "price": 100,
        "name": "Margherita",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    },
    "Tuesday": {
        "price": 200,
        "name": "Carbonara",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    },
    "Wednesday": {
        "price": 320,
        "name": "Calzone",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    },
    "Thursday": {
        "price": 180,
        "name": "Capricciosa",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    },
    "Friday": {
        "price": 299,
        "name": "Gorgonzola",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    },
    "Saturday": {
        "price": 250,
        "name": "Americana",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    },
    "Sunday": {
        "price": 300,
        "name": "Meditterranea",
        "ingredients": [
            "tomatoes",
            "mozzarella",
            "ham"
        ]
    }
}
with open('pizzas.json', 'w') as file:
    json.dump(info, file, indent=4)

with open('pizzas.json', 'r') as file:
    data = json.load(file)


class Pizza:
    """ Class describes a pizza."""

    def __init__(self, day):
        self.day = day
        self.name = data[day]["name"]
        self.price = data[day]["price"]
        self.ingredients = data[day]["ingredients"]

    def add_ingredient(self, *ingredients):
        """ Adds ingredients to pizza and calculates new price."""
        for ingredient in ingredients:
            if ingredient not in data["Ingredients"]:
                raise ValueError("Such ingredient is not available")
            self.ingredients.append(ingredient)
            self.price += data["Ingredients"][ingredient]


class MondayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Monday")


class TuesdayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Tuesday")


class WednesdayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Wednesday")


class ThursdayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Thursday")


class FridayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Friday")


class SaturdayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Saturday")


class SundayPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Sunday")


class Customer:
    """Class describes a customer"""

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return f'customer {self.surname} {self.name} {self.patronymic}'

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


class Order:
    """ Class describes an order."""

    def __init__(self, customer, day):
        self.day = day
        self.pizza = Pizza(day)
        self.customer = customer
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
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Invalid type of day")
        if day not in data.keys():
            raise ValueError("Such day does not exist")
        self.__day = day

    def __str__(self):
        return f'Order for {self.customer}:\n{len(self.pizzas)} pizza(s)-of-the-day ' \
               f'"{self.pizza.name}", total price {self.total_price}\n'

    def buy_pizza_of_the_day(self):
        """Adds appropriate due to day of week pizza to the list"""
        if self.day == 'Monday':
            self.pizza = MondayPizza()
        elif self.day == 'Tuesday':
            self.pizza = TuesdayPizza()
        elif self.day == 'Wednesday':
            self.pizza = WednesdayPizza()
        elif self.day == 'Thursday':
            self.pizza = ThursdayPizza()
        elif self.day == 'Friday':
            self.pizza = FridayPizza()
        elif self.day == 'Saturday':
            self.pizza = SaturdayPizza()
        elif self.day == 'Sunday':
            self.pizza = SundayPizza()
        else:
            raise ValueError("Invalid day of week")

        with open('pizzas.json', 'r') as f:
            pizzas_info = json.load(f)

        self.pizza.ingredients = pizzas_info[self.day]["ingredients"]
        f.close()
        self.pizzas.append(self.pizza)

    @property
    def total_price(self):
        """Returns total price of each order"""
        tmp = 0
        for pizza in self.pizzas:
            tmp += pizza.price
        return tmp


c1 = Customer('Malykhina', 'Iryna', 'Olehivna')
order1 = Order(c1, 'Tuesday')
order1.buy_pizza_of_the_day()
order1.buy_pizza_of_the_day()
order1.pizza.add_ingredient("mushrooms")
order1.buy_pizza_of_the_day()
print(order1)
