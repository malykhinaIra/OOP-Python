import json
from abc import ABC, abstractmethod
from pprint import pprint


class ICourse(ABC):
    """An interface of the course."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Course(ICourse):
    """Class describes a course."""

    def __init__(self, id_number, name, teacher, course_program, course_type):
        self.id_number = id_number
        self.name = name
        self.teacher = teacher
        self.course_program = course_program
        self.course_type = course_type

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if not isinstance(id_number, int):
            raise TypeError("id_number must be an int value")
        if id_number <= 0:
            raise ValueError("Positive numbers only")
        self.__id_number = id_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be str value")
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher must be Teacher value")
        self.__teacher = teacher

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, course_program):
        if not isinstance(course_program, list) or not all(isinstance(x, str) for x in course_program):
            raise TypeError("course_program must be a list of str")
        self.__course_program = course_program

    @property
    def course_type(self):
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


class ILocalCourse(ABC):
    """An interface of the local course."""

    @abstractmethod
    def __init__(self):
        pass


class LocalCourse(Course, ILocalCourse):
    """Class describes a local course."""

    def __init__(self, id_number, name, teacher, course_program, course_type):
        super().__init__(id_number, name, teacher, course_program, course_type)


class IOffsiteCourse(ABC):
    """An interface of the offsite course."""

    @abstractmethod
    def __init__(self):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    """Class describes an offsite course."""

    def __init__(self, id_number, name, teacher, course_program, course_type):
        super().__init__(id_number, name, teacher, course_program, course_type)


class ITeacher(ABC):
    """An interface of the teacher."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def add_course(self, course):
        pass


class Teacher(ITeacher):
    """Class describes a teacher."""

    def __init__(self, id_number, surname, name, patronymic, *courses):
        self.id_number = id_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.courses = courses

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if not isinstance(id_number, int):
            raise TypeError("id_number must be an int value")
        if id_number <= 0:
            raise ValueError("Positive numbers only")
        self.__id_number = id_number

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

    @id_number.setter
    def id_number(self, id_number):
        if not isinstance(id_number, int):
            raise TypeError("id_number must be an int value")
        if id_number <= 0:
            raise ValueError("Positive numbers only")
        self.__id_number = id_number

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = []
        if courses:
            self.__courses = list(courses)

    def add_course(self, course):
        self.courses.append(course)

    def __repr__(self):
        return f'{self.surname} {self.name} {self.patronymic}, courses: {self.courses}'


class ICourseFactory(ABC):
    """An interface of the factory."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_course(self, id_number, name, teacher, course_program, course_type):
        pass

    @abstractmethod
    def create_teacher(self, id_number, surname, name, patronymic, *courses):
        pass


class CourseFactory(ICourseFactory):
    """Class describes a factory to create teachers and courses."""

    def __init__(self):
        self.courses = {}
        self.teachers = {}

    def create_teacher(self, id_number, surname, name, patronymic, *courses):
        with open("teachers.json", 'r') as file:
            self.teachers = json.load(file)
        teacher = Teacher(id_number, surname, name, patronymic, *courses)
        self.teachers[str(teacher.id_number)] = teacher.__dict__
        with open("teachers.json", 'w') as file:
            json.dump(self.teachers, file, indent=5, default=str)
        return teacher

    def create_course(self, id_number, name, teacher, course_program, course_type):
        with open("courses.json", 'r') as file:
            self.courses = json.load(file)
        course_types = {"local": LocalCourse, "offsite": OffsiteCourse}
        course = course_types[course_type](id_number, name, teacher, course_program, course_type)
        teacher.add_course(course.name)
        with open("teachers.json", 'r') as f:
            self.teachers = json.load(f)
        self.teachers[str(teacher.id_number)] = teacher.__dict__
        with open("teachers.json", 'w') as f:
            json.dump(self.teachers, f, default=str, indent=5)
        self.courses[str(course.id_number)] = course.__dict__
        with open("courses.json", 'w') as file:
            json.dump(self.courses, file, default=str, indent=5)
        return course

    def get_course(self, id_number):
        return self.courses[str(id_number)]

    def get_teacher(self, id_number):
        return self.teachers[str(id_number)]


if __name__ == "__main__":
    cf = CourseFactory()
    t1 = cf.create_teacher(3, "Egorov", "Artem", "Olehovych", "Java")
    t2 = cf.create_teacher(4, "Ivanov", "Ivan", "Ihorovych")
    c1 = cf.create_course(4, "Python", t1, ['a', 'b', 'c'], course_type="local")
    c2 = cf.create_course(5, "C#", t2, ['d', 'e', 'f'], course_type="offsite")
    print(c1)
    print(c2)
    print('\n')
    pprint(cf.teachers, sort_dicts=False)
