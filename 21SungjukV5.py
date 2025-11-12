# 성적 처리 프로그램 V4
# 학생의 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점,평균, 학점을 처리한 뒤 결과 출력
# 성적처리의 CRUD를 메뉴식으로 구현
sungjuks=[
    ['혜교', '96.89.99.297.99.99 ','A']
    ['지현', '99.98.97.297.77.82', 'A']
    ['수지', '95.77.77.297.67.62', 'A']
    ]
menus = f'''
--------------------
성적 프로그램 v4
--------------------
1.성적데이터 입력 
2.성적데이터 조회
3.성적데이터 상세조회
4.성적데이터 수정
5.성적데이터 삭제
0.프로그램 종료
--------------------
작업을 선택하세요 :'''

header=''''''

for i in range(1, 100 + 1):
    job = input(menus)

    #   if   job == '1':print('성적데이터 입력을 진행합니다...')
    #  elif job == '2':print('성적데이터 입력을 진행합니다...')
    #   elif job == '3':print('성적데이터 상세조회를 진행합니다...')
    #   elif job == '4':print('성적데이터 수정을 진행합니다...')
    #   elif job ==  '5':print('성적데이터 삭제를 진행합니다...')
    #   elif job ==  '0':print('성적 프로그램을 종료합니다...')
    #   elif job == '0':
    #        print('성적프로그램을 종료합니다...')
    #   else: print ('번호를 잘못입력하셨습니다!')

    match job:
        case '1':
            # 입력
            name = input(f'{i}) 이름을 입력하세요 : ')
            kor = int(input(f'{i}) 국어 점수를 입력하세요 : '))
            eng = int(input(f'{i}) 영어 점수를 입력하세요 : '))
            mat = int(input(f'{i}) 수학 점수를 입력하세요 : '))
            tot = 0
            avg = 0.0
            grd = '가'

            # 성적처리
            tot = kor + eng + mat
            avg = tot / 3
            grd = ('A' if (avg >= 90) else
                   'B' if (avg >= 80) else
                   'C' if (avg >= 70) else
                   'D' if (avg >= 60) else 'F')

            tot = kor + eng + mat
            avg = tot / 3
            grd = ('A' if (avg >= 90) else
                   'B' if (avg >= 80) else
                   'C' if (avg >= 70) else
                   'D' if (avg >= 60) else 'F')

            sj = [name, kor, eng, mat, tot, avg, grd]
            sungjuks.append(sj)

        case '2':
            result = ''

            for name, kor, eng, mat, tot, avg, grd in sungjuks:
                result = f'{name:5s} {kor:4d} {eng:4d} {mat:4d} ' \
                     f'{tot:4d} {avg:.2f} {grd:3s}\n'
            print(f'{header}{result}')

        case '3':
            print('성적데이터 상세조회를 진행합니다...')
        case '4':
            print('성적데이터 수정을 진행합니다...')
        case '5':
            print('성적데이터 삭제를 진행합니다...')
        case '0':
            print('성적프로그램을 종료합니다...')
            break
        case _:
            print('번호를 잘못입력하셨습니다')
