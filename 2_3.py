import itertools


class Student:
    """"Class that contains background information of every student"""

    def __init__(self, name, surname, number, *grades):
        self.name = name
        self.surname = surname
        self.number = number
        self.grades = grades
        self.average = 0

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
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("Invalid type of number")
        if number < 0:
            raise ValueError("Record book number must be positive")
        self.__number = number

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if any(not isinstance(grade, int) for grade in grades) and any(
                not isinstance(grade, float) for grade in grades):
            raise TypeError("Grades must be int or float values")
        if any(grade <= 0 or grade > 12 for grade in grades):
            raise ValueError("Grades must be from 1 to 12")
        self.__grades = grades

    def __str__(self):
        return f'{self.name} {self.surname}, record book number {self.number}, average score: {self.average}'

    def __lt__(self, other):
        return other.get_average() < self.get_average()

    def get_average(self):
        """"Returns student's average score"""
        self.average = sum(self.grades) / len(self.grades)
        return self.average


class Group:

    def __init__(self, students):
        self.students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        if not isinstance(students, list):
            raise TypeError("Invalid type of list")
        if not all(isinstance(student, Student) for student in students):
            raise TypeError("Invalid type of student")
        if len(students) > 20:
            raise OverflowError("There cannot be more than 20 students in a group")
        self.__students = students
        for i, j in itertools.combinations(self.__students, 2):
            if i.surname is j.surname and i.name is j.name:
                raise ValueError(i.surname + ' ' + i.name + ' ' + "is already in the group")

    def add_student(self, student):
        """"Adds each student's data to the list"""
        if not isinstance(student, Student):
            raise TypeError("Invalid type of student")
        if len(self.students) >= 20:
            raise OverflowError("There cannot be more than 20 students in a group")
        if any(student.surname == i.surname for i in self.students) and any(
                student.name == i.name for i in self.students):
            raise ValueError("There is already a student with the same name and surname")
        if any(student.number == i.number for i in self.students):
            raise ValueError("There is already a student with the same record book number")
        self.students.append(student)

    def remove_student(self, student):
        """"Removes each student's data from the list"""
        if not self.students:
            raise ValueError("No students were added yet")
        if not isinstance(student, Student):
            raise TypeError("Invalid type of student")
        self.students.remove(student)

    def top(self):
        """"Returns list of five students with the highest average score"""
        if len(self.students) < 5:
            raise ValueError("Group must have at least 5 students")
        return sorted(self.students)[:5]


s1 = Student('Ivan', 'Ivanov', 1, 5, 10, 7, 8)
s2 = Student('Iryna', 'Malykhina', 2, 3, 4, 5, 7)
s3 = Student('Mykola', 'Kovalyov', 3, 12, 8, 5, 7)
s4 = Student('Hanna', 'Romanova', 4, 5, 8, 4, 3)
s5 = Student('Maria', 'Melnyk', 5, 2, 4, 10, 10)
s6 = Student('Oleh', 'Ivanov', 6, 2, 4, 7, 3)
s7 = Student('Oksana', 'Pashko', 7, 4, 10, 7, 4)
tv_list = [s1, s2, s3, s4, s5]
tv = Group(tv_list)
for el in tv.top():
    print(el)
