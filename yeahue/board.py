counts = 1

menus = f'''
--------------------
    게시판 프로그램 v1
--------------------
   1. 새글쓰기
   2. 게시글 목록
   3. 게시글 본문보기
   4. 게시글 수정하기
   5. 게시글 삭제하기
   6. 프로그램 종료
-----------------------
  작업을 선택하세요: '''

def input_board():
    global counts
    title = input('글제목 :')
    userid = input('작성자:')
    contents = input('본문:')
    board = ['', title, userid, contents, 0, '2025-11-14 17:47:35']
    counts += 1
    return board



def write_board(boards,):
    board = input_board()
    boards.append(board)

    print('글이 등록 되었습니다')

def list_board(boards):
    pass

def view_board(boards):
    bno = int(input('조회할 글번호를 입력하세요:'))
    result ='해당 게시물이 존재하지 않습니다!'

    for bd in boards:
        if bd[0] == bno:
            result ='=====본문 내용 =====\n'
            result+=f'글번호:{bd[0]}\n'
            result += f'글번호:{bd[1]}\n'
            result += f'작성자:{bd[2]}\n'
            result += f'조회수:{bd[4]}\n'
            result += f'작성일{bd[5]}\n'
            result += f'본문:{bd[3]}\n'
    print(result)

def modify_board(boards):
    bno = int(input('수정할 글번호를 입력하세요:'))
    result ='해당 게시물이 존재하지 않습니다!'

    for bd in boards:
        if bd[0] == bno:
            new_title=input(f'새 본문 :({bd[3]})')
            new_contents = input(f'새 본문 :({bd[3]})')
            bd[1]=new_title
            bd[3]=new_contents
            result = '해당 게시물을 수정되었습니다!'

    print(result)

    

def remove_board(boards):
    bno = int(input('삭제할 글번호를 입력하세요:'))
    result = '해당 게시물이 존재하지 않습니다!'

    for bd in boards:
        if bd[0] == bno:
            boards.remove(bd)   # !!
            result ='해당 게시물을 삭제했습니다!'

    print(result)

    pass





