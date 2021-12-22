from interfaces import *
from courses import *


class Teacher(ITeacher):
    """Class describes a teacher."""

    def __init__(self, id_number: int, surname: str, name: str, patronymic: str, *courses):
        self.id_number = id_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.courses = courses

    @property
    def id_number(self) -> int:
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if not isinstance(id_number, int):
            raise TypeError("id_number must be an int value")
        if id_number <= 0:
            raise ValueError("Positive numbers only")
        self.__id_number = id_number

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Invalid type of surname")
        if any(map(str.isdigit, surname)):
            raise ValueError("Invalid surname")
        self.__surname = surname

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid type of name")
        if any(map(str.isdigit, name)):
            raise ValueError("Invalid name")
        self.__name = name

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Invalid type of patronymic")
        if any(map(str.isdigit, patronymic)):
            raise ValueError("Invalid patronymic")
        self.__patronymic = patronymic

    @id_number.setter
    def id_number(self, id_number):
        if not isinstance(id_number, int):
            raise TypeError("id_number must be an int value")
        if id_number <= 0:
            raise ValueError("Positive numbers only")
        self.__id_number = id_number

    @property
    def courses(self) -> list[str]:
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = []
        if courses:
            self.__courses = list(courses)

    def add_course(self, course):
        self.courses.append(course)

    def __repr__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}, courses: {self.courses}'