# 32 주민번호 검사 - 리스트, 컴프리헨션으로 재작성
# 문자가 숫자인지 확인 :isdigit()
jumin ='450124-1234569'
sum = 0

# a.b
code =[]
#for j in jumin:
#    if j.isdigit():
#        code.append(int(j))
code =[int(j) for j in jumin if j.isdigit()]

print(f'추출된 주민번호: {code}')

# wght = [2,3,4,5,6,7,8,9,2,3,4,5]
# wght == []
# for i in range(12):
#    wght.append((i % 8) + 2 )

print('자동생성된 가중치: {wght}')

for i in range(12):




    print(sum)

    # c,d

    checker = 11 -(sum % 11)
    print(checker, str(checker)[-1])

    #5. 결과 출력
    print(f'계산된 검증번호:{checker}')
    print(f'입력된 검증번호:{code[-1]}')
    print(f'유효한 주민등록번호입니다.'if checker == code[-1] else '잘못된 주민등록번호입니다.')
