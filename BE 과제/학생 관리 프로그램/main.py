from student import *
from managerService import StudentManagerService


def main(manager):  # manager: StudentManagerImpl 클래스의 객체
    while True:
        print("=" * 15)
        print("1. 학생 추가")
        print("2. 전체 학생 조회")
        print("3. 학생 검색")
        print("4. 학생 삭제")
        print("5. 학생 정보 수정")
        print("6. 종료")
        print("=" * 15)

        command = int(input())
        if command == 1:
            print("등록할 학생 정보를 입력해주세요")
            student_id = input("학번: ")
            name = input("이름: ")
            age = input("나이: ")
            major = input("전공: ")
            grade = input("학점: ")
            student = Student(student_id, name, age, major, grade)
            manager.add_student(student)
            print(f"{name} 학생이 추가되었습니다.")

        elif command == 2:
            students = manager.list_student()
            if len(students) == 0:
                print("등록된 학생이 없습니다.")
            else:
                print("<<전체 학생 리스트>>")
                for student in students:
                    print(f"이름: {student.get_name()}, 학점: {student.get_grade()}")  # 학점에 따라 정렬이 되는지 확인

        elif command == 3:
            student_id = input("조회할 학생의 학번을 입력해주세요: ")
            if manager.search_student(student_id):
                students = manager.search_student(student_id)
                for student in students:
                    print(f"이름: {student.get_name()}")
                    print(f"나이: {student.get_age()}")
                    print(f"전공: {student.get_major()}")
                    print(f"학점: {student.get_grade()}")
            else:
                print("해당 학번을 가진 학생은 존재하지 않습니다")

        elif command == 4:
            student_id = input("삭제할 학생의 학번을 입력해주세요: ")
            if manager.search_student(student_id):
                manager.delete_student(student_id)
                print("학생 정보가 삭제되었습니다.")
            else:
                print("해당 학번을 가진 학생은 존재하지 않습니다")

        elif command == 5:
            student_id = input("수정할 학생의 학번을 입력해주세요: ")
            while True:  # 입력한 학번이 존재하는지 검사
                existing_id = manager.search_student(student_id)
                if existing_id:
                    new_student_id = input("새로운 학번을 입력해주세요: ")
                    if manager.search_student(new_student_id):
                        print(f"{new_student_id} 학번은 이미 존재합니다. 다른 학번을 입력해주세요.")
                    else:
                        name = input("수정할 이름을 입력해주세요: ")
                        age = input("수정할 나이를 입력해주세요: ")
                        major = input("수정할 전공을 입력해주세요: ")
                        grade = input("수정할 학점을 입력해주세요: ")
                        new_student = Student(new_student_id, name, age, major, grade)
                        manager.update_student(student_id, new_student)
                        print(f"{name} 학생 정보가 수정되었습니다.")
                        break
                else:
                    print("존재하지 않는 학번입니다.")
                    break

        elif command == 6:
            print("학생 관리 프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")


if __name__ == '__main__':
    manager = StudentManagerService()
    main(manager)
