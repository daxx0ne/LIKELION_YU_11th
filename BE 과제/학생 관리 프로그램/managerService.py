from managerImpl import StudentManagerImpl


class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentManagerImpl()

    def add_student(self, student):  # 학생 추가
        self.__student_repo.add_student(student)

    def list_student(self):  # 전체 학생 조회
        return self.__student_repo.list_student()

    def search_student(self, student_id):  # 학생 조회
        return self.__student_repo.search_student(student_id)

    def delete_student(self, student_id):  # 학생 제거
        self.__student_repo.delete_student(student_id)

    def update_student(self, student_id, student):  # 학생 수정
        self.__student_repo.update_student(student_id, student)
