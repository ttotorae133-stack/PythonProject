# 게시판 앱 v1
# 글번호, 글제목 ,작성자 ,본문, 조회수, 작성일"형식의
# 게시판 데이터를 생성,조회 수정 ,삭제하는 프로그램
# 새글쓰기 :글제목, 작성자 ,본문
# 게시판 목록: 글번호, 글제목 ,작성자 ,본문, 조회수, 작성일(년원일)
# 본문보기: 글번호, 글제목, 작성자, 조회수 ,작성일,본문
from yeahue.board import menus
from yeahue.board import write_board
from yeahue.board import list_board
from yeahue.board import view_board
from yeahue.board import modify_board
from yeahue.board import remove_board

boards = []


header1='''
       ===== 게시글 목록 ======
번호  | 제목 |  작성자 |  작성일 | 조회
----------------------------------
'''

while True:
    job = input(menus)


    match job:
        case'1':
            write_board(boards)

        case'2':
            list_board(boards)

        case'3':
           view_board(boards)

        case'4':
            modify_board(boards)


        case'5':
            remove_board(boards)

        case'0': break
        case _: print('번호를 잘못 입력하셨습니다!!')