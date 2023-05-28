# View & Test case

### 💻 CODE REVIEW

Reviewer: 

1.

---
### ⬇️ 실행 결과

1. `test_post_list_view`: post_list 뷰 테스트
   
   - post_list 뷰는 게시글 목록을 조회하는 기능을 담당
   - 해당 뷰를 호출했을 때 응답 상태 코드가 200인지 확인


2. `test_post_detail_view`: post_detail 뷰 테스트

   - post_detail 뷰는 특정 게시글의 상세 정보를 (하나만) 조회하는 기능을 담당
   - 특정 게시글의 상세 정보를 조회했을 때 응답 상태 코드가 200인지 확인


3. `test_post_create_view`: post_create 뷰 테스트

   - post_create 뷰는 게시글을 생성하는 기능을 담당
   - 이 테스트는 게시글 생성 폼을 렌더링했을 때 응답 상태 코드가 200인지 확인
   - 유효한 데이터를 전송하여 게시글을 생성하면 응답 상태 코드가 302(리다이렉트)인지 확인
   - 생성된 게시글이 예상대로 저장되었는지 확인


4. `test_post_update_view`: post_update 뷰 테스트 

   - post_update 뷰는 게시글을 업데이트하는 기능을 담당
   - 게시글 수정 폼을 렌더링(작성한 html이 브라우저에서 출력되는 과정)했을 때 응답 상태 코드가 200인지 확인
   - 유효한 데이터를 전송하여 게시글을 업데이트하면 응답 상태 코드가 302(리다이렉트)인지 확인
   - 게시글이 예상대로 업데이트되었는지 확인


5. `test_post_delete_view`: post_delete 뷰 테스트

   - post_delete 뷰는 게시글을 삭제하는 기능을 담당
   - 특정 게시글 삭제를 요청했을 때 응답 상태 코드가 302(리다이렉트)인지 확인
   - 게시글이 정상적으로 삭제되었는지 확인


