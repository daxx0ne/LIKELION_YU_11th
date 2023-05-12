class Student:
    def __init__(self, student_id, name, age, major, grade):
        self.__student_id = student_id  # 학생의 학번
        self.__name = name  # 학생의 이름
        self.__age = age  # 학생의 나이
        self.__major = major  # 학생의 전공
        self.__grade = grade  # 학생의 학점

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_major(self):
        return self.__major

    def get_grade(self):
        return self.__grade