from abc import ABC, abstractmethod


class ICourse(ABC):
    """An interface of the course."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):
    """An interface of the local course."""

    @abstractmethod
    def __init__(self):
        pass


class IOffsiteCourse(ABC):
    """An interface of the offsite course."""

    @abstractmethod
    def __init__(self):
        pass


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
