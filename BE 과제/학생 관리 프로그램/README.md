# 학생 관리 프로그램

### 💻 CODE REVIEW

Reviewer: 남은주

1. 과제의 목표가 객체지향인 만큼, 코드를 작성할 때 class를 각각 다른 파일로 만들었으면 좋았을 것 같다.
2. 학생 추가 시 등록된 학생을 고려하여 예외처리를 한 점이 좋았다.
3. 전체 학생 출력 시 학생 정렬 기능을 추가한 점이 새로웠다.
4. `StudentManagerImpl` 클래스에서 학생 찾는 기능의 `search_student`의 리스트 변수명을 왜 `result`로 설정하셨는지 궁금하다.

    -> `result`로 변수명을 써놓은 것이 직관적이지 못하다는 생각이 들었다. 코드를 짜다가 생각없이 결과를 반환해줘야 하니 `result`로 썼는데 기능 구현이 된 걸 보고 꼼꼼히 확인을 못한 것 같다!
    - [ ] `search_student`의 리스트 변수명 수정하기
  
  
5. main 함수에서 학생의 정보를 조회하거나 삭제 및 수정할 때, 왜 학번을 사용하셨는지 궁금하다. 또, 학번을 사용하여 학생의 정보에 접근하였으므로 `StudentManagerRepo` 클래스와  `StudentManagerService` 부분에 함수의 `name` 매개변수의 이름도 `student_id`로 수정을 고려하였는지도 궁금하다.

    -> 처음엔 `name`을 기준으로 CRUD 를 구현해보려고 했는데 생각해보니, 동명이인이 있을 때 기능 구현에 있어서 곤란한 점이 생길 것 같아, 임의로 학번을 고유키(?) 처럼 지정해서 코드를 짰다. `StudentManagerRepo` 클래스와 `StudentManagerService` 클래스의 변수명은 적절하게 바꿔야겠다! (제공받은 코드는 수정하면 안되는 줄 알았다..) 
    - [ ] `StudentManagerRepo` 클래스와 `StudentManagerService` 클래스의 변수명 수정하기

---
### ⬇️ 실행 결과

**1. CREATE**

![스크린샷 2023-05-10 오전 9 15 57](https://github.com/daxx0ne/LIKELION_YU_11th/assets/117694148/9b58651d-a707-4a71-bdcf-7f1ffbf5a6fb)
<br>

**2. READ**

![스크린샷 2023-05-10 오전 9 16 24](https://github.com/daxx0ne/LIKELION_YU_11th/assets/117694148/366503f2-843f-4ce0-9a99-46fc7604e36a)
<br>

**3. UPDATE**

![스크린샷 2023-05-10 오전 9 28 14](https://github.com/daxx0ne/LIKELION_YU_11th/assets/117694148/f18d86c6-4ebe-494c-9621-c10a6cebc37c)
<br>

**4. DELETE**

![스크린샷 2023-05-10 오전 9 24 57](https://github.com/daxx0ne/LIKELION_YU_11th/assets/117694148/c7903e3e-d3a8-4e16-9d8d-83ecc631536b)
<br>

**5. EXIT**

![스크린샷 2023-05-10 오전 9 28 20](https://github.com/daxx0ne/LIKELION_YU_11th/assets/117694148/c9dd88d2-92cd-42fb-b43a-4478c20a6d17)
