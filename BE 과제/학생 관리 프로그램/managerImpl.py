from managerRepo import StudentManagerRepo


class StudentManagerImpl(StudentManagerRepo):  # 학생 정보를 관리하는 클래스
    def __init__(self):
        self.__students = []

    def add_student(self, student):  # 학생 객체를 받아서 학생의 학번을 검사한 후, 등록되지 않은 학번인 경우 학생을 리스트에 추가
        student_id = student.get_student_id()
        if any(s.get_student_id() == student_id for s in self.__students):
            raise ValueError(f"{student_id}은 이미 등록된 학번입니다.")
        self.__students.append(student)

    def list_student(self):
        sorted_students = sorted(self.__students, key=lambda x: x.get_grade(), reverse=True)
        return sorted_students  # 학점에 따라 학생을 정렬하는 기능을 추가함

    def search_student(self, student_id):
        search_result = []
        for student in self.__students:
            if student.get_student_id() == student_id:
                search_result.append(student)
        return search_result

    def delete_student(self, student_id):
        for i, student in enumerate(self.__students):
            if student.get_student_id() == student_id:
                del self.__students[i]

    def update_student(self, student_id, student):
        for i, s in enumerate(self.__students):
            if s.get_student_id() == student_id:
                self.__students[i] = student
