# 컴프리헨션
# 시퀀스 자료형(리스트, 딕셔너리등)에서
# 한줄 코드로 간결하게 생성, 관리하는 문법

person= ['혜교''123-4567-8912','abc@abc.co.kr']

for i in range(3):
    print(person[i],end= ' ')
    print()

# [표현식 for 변수 in 반복가능객체]
[print(p, end =' ') for p in person]


