import json
from pprint import pprint
import jsonschema
from jsonschema import validate
from courses import *
from teacher import *


class CourseFactory(ICourseFactory):
    """Class describes a factory to create teachers and courses."""

    def __init__(self):
        self.courses = {}
        self.teachers = {}
        self.json_file = JsonFile()

    def create_teacher(self, id_number: int, surname: str, name: str, patronymic: str, *courses) -> Teacher:
        self.teachers = self.json_file.file_read("teachers.json", self.teachers)
        teacher = Teacher(id_number, surname, name, patronymic, *courses)
        self.json_file.json_validate(teacher)
        self.teachers[str(teacher.id_number)] = teacher.__dict__
        self.json_file.file_write("teachers.json", self.teachers)
        return teacher

    def create_course(self, id_number: int, name: str, teacher: Teacher, course_program: list[str],
                      course_type: str) -> Course:
        course_types = {"local": LocalCourse, "offsite": OffsiteCourse}
        course = course_types[course_type](id_number, name, teacher, course_program, course_type)
        self.courses = self.json_file.file_read("courses.json", self.courses)
        self.teachers = self.json_file.file_read("teachers.json", self.teachers)
        teacher.add_course(course.name)
        self.json_file.json_validate(teacher)
        self.teachers[str(teacher.id_number)] = teacher.__dict__
        self.json_file.file_write("teachers.json", self.teachers)
        self.json_file.json_validate(course)
        self.courses[str(course.id_number)] = course.__dict__
        self.json_file.file_write("courses.json", self.courses)
        return course

    def get_course(self, id_number: int) -> dict:
        return self.courses[str(id_number)]

    def get_teacher(self, id_number: int) -> dict:
        return self.teachers[str(id_number)]


class JsonFile:
    """Class describes a json file"""
    def __init__(self):
        self.teacher_schema = {
            "type": "object",
            "title": "The teacher schema",
            "default": {},
            "examples": [
                {
                    "id_number": 3,
                    "surname": "Egorov",
                    "name": "Artem",
                    "patronymic": "Olehovych",
                    "_Teacher__courses": [
                        "Java",
                        "Python"
                    ]
                }
            ],
            "required": [
                "id_number",
                "surname",
                "name",
                "patronymic",
                "_Teacher__courses"
            ],
            "properties": {
                "id_number": {
                    "type": "integer",
                    "title": "The id_number schema",
                    "default": 0,
                    "examples": [
                        3
                    ]
                },
                "surname": {
                    "type": "string",
                    "title": "The surname schema",
                    "default": "",
                    "examples": [
                        "Egorov"
                    ]
                },
                "name": {
                    "type": "string",
                    "title": "The name schema",
                    "default": "",
                    "examples": [
                        "Artem"
                    ]
                },
                "patronymic": {
                    "type": "string",
                    "title": "The patronymic schema",
                    "default": "",
                    "examples": [
                        "Olehovych"
                    ]
                },
                "_Teacher__courses": {
                    "type": "array",
                    "title": "The _Teacher__courses schema",
                    "default": [],
                    "examples": [
                        [
                            "Java",
                            "Python"
                        ]
                    ]
                }
            }
        }
        self.course_schema = {
            "type": "object",
            "title": "The course schema",
            "default": {},
            "examples": [
                {
                    "id_number": 1,
                    "name": "Java",
                    "teacher": "Kovaliov Mykola Serhiiovych, courses: ['Java']",
                    "course_program": [
                        "a",
                        "b",
                        "c"
                    ],
                    "course_type": "local"
                }
            ],
            "required": [
                "id_number",
                "name",
                "teacher",
                "course_program",
                "course_type"
            ],
            "properties": {
                "id_number": {
                    "type": "integer",
                    "title": "The id_number schema",
                    "default": 0,
                    "examples": [
                        1
                    ]
                },
                "name": {
                    "type": "string",
                    "title": "The name schema",
                    "default": "",
                    "examples": [
                        "Java"
                    ]
                },
                "course_program": {
                    "type": "array",
                    "title": "The course_program schema",
                    "default": [],
                    "examples": [
                        [
                            "a",
                            "b"
                        ]
                    ]
                },
                "course_type": {
                    "type": "string",
                    "title": "The course_type schema",
                    "default": "",
                    "examples": [
                        "local"
                    ]
                }
            }
        }

    def json_validate(self, value):
        try:
            if isinstance(value, Teacher):
                validate(instance=value.__dict__, schema=self.teacher_schema)
            elif isinstance(value, Course):
                validate(instance=value.__dict__, schema=self.course_schema)
            else:
                raise TypeError
        except jsonschema.exceptions.ValidationError as e:
            raise e

    @staticmethod
    def file_write(file_name, value):
        with open(file_name, 'w') as file:
            json.dump(value, file, default=str, indent=5)

    @staticmethod
    def file_read(file_name, value) -> dict:
        with open(file_name, 'r') as file:
            value = json.load(file)
        return value


if __name__ == "__main__":
    cf = CourseFactory()
    t1 = cf.create_teacher(3, "Egorov", "Artem", "Olehovych", "Java")
    t2 = cf.create_teacher(4, "Ivanov", "Ivan", "Ihorovych")
    c1 = cf.create_course(4, "Python", t1, ['a', 'b', 'c'], course_type="local")
    c2 = cf.create_course(5, "C#", t2, ['d', 'e', 'f'], course_type="offsite")

    print(cf.get_course(2))
    pprint(cf.courses, sort_dicts=False)
