# 게시글을 저장할 리스트 (boards)
boards = []


# 게시글 클래스 정의
class Post:
    def __init__(self, title, content, author):
        self.title = title  # 게시글 제목
        self.content = content  # 게시글 내용
        self.author = author  # 게시글 작성자

    def __str__(self):
        # 게시글 정보 출력 형식
        return f"제목: {self.title}\n작성자: {self.author}\n내용:\n{self.content}\n"


# 게시글 작성 함수
def write_post():
    title = input("게시글 제목을 입력하세요: ")
    content = input("게시글 내용을 입력하세요: ")
    author = input("작성자를 입력하세요: ")

    # Post 객체 생성 후 boards 리스트에 추가
    new_post = Post(title, content, author)
    boards.append(new_post)
    print("게시글이 작성되었습니다.")


# 게시글 조회 함수
def view_posts():
    if not boards:
        print("게시글이 없습니다.")
        return

    # 모든 게시글 출력
    for i, post in enumerate(boards):
        print(f"\n{(i + 1)}번째 게시글")
        print(post)


# 게시글 수정 함수
def modify_post():
    post_id = int(input("수정할 게시글 번호를 입력하세요: ")) - 1

    if 0 <= post_id < len(boards):
        title = input("새로운 제목을 입력하세요: ")
        content = input("새로운 내용을 입력하세요: ")
        author = input("새로운 작성자를 입력하세요: ")

        # 기존 게시글 수정
        boards[post_id].title = title
        boards[post_id].content = content
        boards[post_id].author = author

        print("게시글이 수정되었습니다.")
    else:
        print("잘못된 게시글 번호입니다.")


# 게시글 삭제 함수
def delete_post():
    post_id = int(input("삭제할 게시글 번호를 입력하세요: ")) - 1

    if 0 <= post_id < len(boards):
        boards.pop(post_id)
        print("게시글이 삭제되었습니다.")
    else:
        print("잘못된 게시글 번호입니다.")


# 메인 메뉴
def menu():
    while True:
        print("\n게시판 프로그램")
        print("1. 게시글 작성")
        print("2. 게시글 조회")
        print("3. 게시글 수정")
        print("4. 게시글 삭제")
        print("5. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            write_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            modify_post()
        elif choice == "4":
            delete_post()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


# 프로그램 시작
if __name__ == "__main__":
    menu()
