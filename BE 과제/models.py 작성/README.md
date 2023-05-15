# 개인 블로그 모델링 하고 models.py 작성

### 💻 CODE REVIEW

Reviewer: 이진우

1. **date_created, date_modified**
    - 생성 및 수정 칼럼의 일반적인 컨벤션은 created_at, updated_at을 사용함
    (참고 : MySQL 컨벤션 [https://velog.io/@peppermint100/MySQL-Naming-Convention-번역](https://velog.io/@peppermint100/MySQL-Naming-Convention-%EB%B2%88%EC%97%AD))
2. **post 테이블에 author가 있어야 하는가?**
    - 블로그는 일반적으로 블로그 주인만 게시글 생성이 가능함
    - 그렇기 때문에 post 테이블에 author 컬럼이 있어야 할까요?
3. **post 테이블에 FK default가 1이어야 하는가?**
    - author default를 null로 두는 것이 더 좋을 것 같음
4. **Post 테이블의 tag 컬럼의 관계 변경?**
    - "다대다 관계는 “미완성된 모델링”이라 간주하며 중재 테이블을 놓아 다대다 관계를 회피하는 것이 좋다." 라고 교육 자료에 있어서 다대다를 없애고 PostTag 혹은 post_tag 테이블을 만드는게 좋지 않을까?
5. **Post 테이블에 조회 수 컬럼 추가**
    - 게시글의 경우 조회수가 출력되는 경우도 있으므로 만들어봐도 좋을 것 같음

---
### ⬇️ 실행 결과

**Django admin Page에서 확인**

![스크린샷 2023-05-12 오후 2 31 58](https://github.com/daxx0ne/LIKELION_YU_11th/assets/117694148/dd635762-525e-42bc-9422-7f7951f48256)

### 🔍 모델 & 필드 설명

- **Blog**
  - `title`: 블로그 제목을 나타내는 CharField (20자로 제한)
  - `description`: 블로그 소개글을 나타내는 CharField (100자로 제한)
    - 비어있을 수 있도록 null=True로 설정
  - `date_created`: 블로그가 생성된 날짜와 시간을 나타내는 DateTimeField
    - auto_now_add=True로 지정하여 자동으로 생성 시간을 저장
  - `date_modified`: 블로그가 수정된 날짜와 시간을 나타내는 DateTimeField
    - auto_now=True로 지정하여 자동으로 수정 시간을 저장
  - `author`: 해당 블로그 작성자를 나타내는 ForeignKey (User 모델과의 연결)
    - on_delete 옵션으로 CASCADE를 사용하여, User 모델과 연결된 Blog가 삭제되면 해당 User 모델의 데이터도 함께 삭제
  - `available_blogs`: 한 계정이 만들 수 있는 최대 블로그의 개수를 나타내는 PositiveIntegerField (양수값만 저장 가능 / 기본값 1, 최대값 3)
    - validators = [MaxValueValidator(3)] -> 유효성 검사기를 통해 해당 필드의 값이 최대값(3)을 초과하지 않도록 제한


- **Post**
  - `title`: 게시글 제목을 나타내는 CharField (30자로 제한)
  - `body`: 게시글 내용을 나타내는 TextField
  - `date_created`: 게시글이 생성된 날짜와 시간을 나타내는 DateTimeField
    - auto_now_add=True로 설정하여 게시글 생성시 현재 시간을 자동으로 입력
  - `date_modified`: 게시글이 수정된 날짜와 시간을 나타내는 DateTimeField
    - auto_now=True로 설정하여 게시글 수정시 현재 시간을 자동으로 업데이트
  - `author`: 게시글 작성자를 나타내는 ForeignKey (User 모델과의 연결)
    - User 객체가 삭제될 경우 해당 게시글도 함께 삭제
  - `blog`: 게시글이 속한 블로그를 나타내는 ForeignKey (Blog 모델과의 연결)
    - Blog 객체가 삭제될 경우 해당 게시글도 함께 삭제
  - `tags`: 게시글에 적용된 태그를 나타내는 ManyToManyField (Tag 모델과의 연결)
    - Tag 모델과 다대다 관계를 가지며, tags 필드를 통해 중간 테이블을 생성하여 게시글과 태그의 관계를 나타냄


- **Comment**
  - `comment`: 댓글 내용을 나타내는 CharField (100자로 제한)
  - `date_created`: 댓글이 생성된 날짜와 시간을 나타내는 DateTimeField
  - `date_modified`: 댓글이 수정된 날짜와 시간을 나타내는 DateTimeField
  - `author`: 댓글 작성자를 나타내는 ForeignKey (User 모델과의 연결)
    - 댓글 작성자가 삭제될 경우 해당 댓글도 함께 삭제
  - `post`: 댓글이 속한 게시글을 나타내는 ForeignKey (Post 모델과의 연결)
    - 게시글이 삭제될 경우 해당 게시글에 달린 모든 댓글도 함께 삭제


- **Tag**
  - `tag`: 태그 명을 나타내는 CharField (10자로 제한)
  - `blog`: 태그가 속한 블로그를 나타내는 ForeignKey (Blog 모델과의 연결)
    - 블로그가 삭제될 경우 해당 블로그에서 생성한 모든 태그도 함께 삭제


- **Category**
  - `category`: 카테고리 명을 나타내는 CharField (20자로 제한)
  - `blog`: 카테고리가 속한 블로그를 나타내는 ForeignKey (Blog 모델과의 연결)
    - 블로그가 삭제될 경우 해당 카테고리도 함께 삭제

- **Like**
  - `user`: 공감을 누른 사용자를 나타내는 ForeignKey (User 모델과의 연결)
  - `post`: 공감을 누른 게시글을 나타내는 ForeignKey (Post 모델과의 연결)
  - `date`: 공감이 눌러진 날짜와 시간을 나타내는 DateTimeField


- **Subscription**
  - `user`: 구독을 누른 사용자를 나타내는 ForeignKey (User 모델과의 연결)
  - `blog`: 구독을 누른 게시글을 나타내는 ForeignKey (Post 모델과의 연결)
  - `date`: 구독이 눌러진 날짜와 시간을 나타내는 DateTimeField
