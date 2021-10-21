class Student:
    """"Class that contains background information of every student"""
    def __init__(self, name, surname, number, *grades):
        if not isinstance(surname, str) or not isinstance(name, str):
            raise TypeError("Name and surname must be string values")
        if any(map(str.isdigit, surname)) or any(map(str.isdigit, name)):
            raise ValueError("Invalid name or surname")
        if not isinstance(number, int):
            raise TypeError("Record book number must be int value")
        if number < 0:
            raise ValueError("Record book number must be positive")
        if any(not isinstance(grade, int) for grade in grades) and any(
                not isinstance(grade, float) for grade in grades):
            raise TypeError("Grades must be int or float values")
        if any(grade <= 0 or grade > 12 for grade in grades):
            raise ValueError("Grades must be from 1 to 12")
        self.name = name
        self.surname = surname
        self.number = number
        self.grades = grades
        self.average = 0

    def __str__(self):
        return f'{self.name} {self.surname}, record book number {self.number}, average score: {self.average}'

    def __lt__(self, other):
        return self.get_average() > other.get_average()

    def get_average(self):
        """"Returns student's average score"""
        self.average = sum(self.grades) / len(self.grades)
        return self.average


class Group:

    def __init__(self):
        self.students = list()
        self.top_five = list()

    def add_student(self, student):
        """"Adds each student's data to the list"""
        if not isinstance(student, Student):
            raise TypeError("Invalid type of student")
        if len(self.students) == 21:
            raise OverflowError("There cannot be more than 20 students in a group")
        if any(student.surname == i.surname for i in self.students) and any(
                student.name == i.name for i in self.students):
            raise ValueError("There is already a student with the same name and surname")
        if any(student.number == i.number for i in self.students):
            raise ValueError("There is already a student with the same name and surname")
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
        self.students.sort()
        for i in range(5):
            self.top_five.append(self.students[i])
        return self.top_five

    def print_top(self):
        """"Displays list of five students with the highest average score"""
        for el in self.top_five:
            print(el)


s1 = Student('Ivan', 'Ivanov', 1, 5, 10)
s2 = Student('Kateryna', 'Romanove', 2, 3, 4, 5, 7, 12)
s3 = Student('Mykola', 'Kovalyov', 3, 12, 8, 5, 7, 10)
s4 = Student('Hanna', 'Romanova', 4, 5)
s5 = Student('Maria', 'Melnyk', 5, 2, 4, 10, 10, 10)
s6 = Student('Oleh', 'Ivanov', 6, 2, 4, 5, 7, 3)
s7 = Student('Oksana', 'Pashko', 7, 4, 10, 7, 4)

a = Group()
a.add_student(s1)
a.add_student(s2)
a.add_student(s3)
a.add_student(s4)
a.add_student(s5)
a.add_student(s6)
a.add_student(s7)

a.top()
a.print_top()
