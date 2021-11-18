from pprint import pprint
import uuid
from datetime import datetime, date
import json
from coefficients import *


class Customer:
    """Class describes a customer"""
    def __init__(self, surname, name, patronymic, student=False):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.student = student

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

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        if not isinstance(student, bool):
            raise TypeError("Invalid type of student")
        self.__student = student


class Ticket:
    """Class describes a ticket"""
    def __init__(self, customer, event):
        self.id = str(uuid.uuid4().fields[-1])[:5]
        self.customer = customer
        self.event = event
        self.price = self.event.price

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Invalid type of customer")
        self.__customer = customer

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event):
        if not isinstance(event, Event):
            raise TypeError("Invalid type of event")
        self.__event = event

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError("Invalid type of price")
        self.__price = price

    def __str__(self):
        return f'{self.customer}, price: {self.price}, date of event "{self.event.name}": {self.event.event_date}'


class Event:
    """Class describes an event"""
    def __init__(self, name):
        self.name = name
        self.event_date = data[name]['event_date']
        self.price = data[name]['price']

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid type of name")
        self.__name = name

    def __str__(self):
        return f'{self.name} {self.event_date}'


class Order:
    """Class describes an order"""
    def __init__(self, event_name, customer):
        self.event = Event(event_name)
        self.customer = customer
        self.ticket = Ticket(customer, self.event)
        self.current_date = str(date.today().__format__("%d.%m.%Y"))

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Invalid type of customer")
        self.__customer = customer

    def __str__(self):
        return f'{self.name} {self.event_date}'

    def count_date(self):
        """Returns a difference between two dates"""
        event_date = datetime.strptime(self.event.event_date, "%d.%m.%Y")
        current_date = datetime.strptime(self.current_date, "%d.%m.%Y")
        return abs((event_date - current_date).days)

    def sell_ticket(self):
        """ Adds appropriate ticket to the dictionary."""
        if datetime.strptime(self.event.event_date, "%d.%m.%Y") < datetime.strptime(self.current_date, "%d.%m.%Y"):
            raise ValueError("Event has already past")
        if self.customer.student is True:
            self.ticket = StudentTicket(self.customer, self.event)
        elif self.count_date() <= LATE_DAYS:
            self.ticket = LateTicket(self.customer, self.event)
        elif self.count_date() >= ADVANCE_DAYS:
            self.ticket = AdvanceTicket(self.customer, self.event)
        tickets.update({self.ticket.id: self.ticket.__dict__})
        # with open('sold_tickets.json', "w") as f:
        #     json.dump(tickets, f, indent=3, default=str)

    def construct_ticket(self, ticket_id):
        """Returns a ticket by number"""
        with open('sold_tickets.json', 'r') as f:
            x = json.load(f)[ticket_id]
        return x


class AdvanceTicket(Ticket):
    def __init__(self, customer, event):
        super().__init__(customer, event)
        self.price *= ADVANCE_DISCOUNT


class StudentTicket(Ticket):
    def __init__(self, customer, event):
        super().__init__(customer, event)
        self.price *= STUDENT_DISCOUNT


class LateTicket(Ticket):
    def __init__(self, customer, event):
        super().__init__(customer, event)
        self.price *= LATE_DISCOUNT


with open('events.json', 'r') as file:
    data = json.load(file)
tickets = {}

c1 = Customer('Malykhina', 'Iryna', 'Olehivna')
c2 = Customer('Melnyk', 'Oksana', 'Romanivna', student=True)
order1 = Order('Event1', c1)
order2 = Order('Event2', c1)
order3 = Order('Event2', c2)
order1.sell_ticket()
order2.sell_ticket()
order3.sell_ticket()

print(order1.ticket)
print(order2.ticket)
print(order3.ticket)
# pprint(order2.construct_ticket("70833"))
