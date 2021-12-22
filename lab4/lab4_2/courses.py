from teacher import *


class Course(ICourse):
    """Class describes a course."""

    def __init__(self, id_number: int, name: str, teacher: Teacher, course_program: list[str], course_type: str):
        self.id_number = id_number
        self.name = name
        self.teacher = teacher
        self.course_program = course_program
        self.course_type = course_type

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be str value")
        self.__name = name

    @property
    def teacher(self) -> Teacher:
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher must be Teacher value")
        self.__teacher = teacher

    @property
    def course_program(self) -> list[str]:
        return self.__course_program

    @course_program.setter
    def course_program(self, course_program):
        if not isinstance(course_program, list) or not all(isinstance(x, str) for x in course_program):
            raise TypeError("course_program must be a list of str")
        self.__course_program = course_program

    @property
    def course_type(self) -> str:
        return self.__course_type

    @course_type.setter
    def course_type(self, course_type):
        if not isinstance(course_type, str):
            raise TypeError("course_type must be str value")
        if course_type not in ("offsite", "local"):
            raise ValueError("Invalid course_type")
        self.__course_type = course_type

    def __str__(self):
        return f'{self.course_type} course "{self.name}", teacher: {self.teacher.surname} ' \
               f'{self.teacher.name} {self.teacher.patronymic}\nProgram of the course: {self.course_program}'

    def __str__(self) -> str:
        return f'{self.course_type} course "{self.name}", teacher: {self.teacher.surname} ' \
               f'{self.teacher.name} {self.teacher.patronymic}\nProgram of the course: {self.course_program}'


class LocalCourse(Course, ILocalCourse):
    """Class describes a local course."""

    def __init__(self, id_number: int, name: str, teacher: Teacher, course_program: list[str], course_type: str):
        super().__init__(id_number, name, teacher, course_program, course_type)


class OffsiteCourse(Course, IOffsiteCourse):
    """Class describes an offsite course."""

    def __init__(self, id_number: int, name: str, teacher: Teacher, course_program: list[str], course_type: str):
        super().__init__(id_number, name, teacher, course_program, course_type)