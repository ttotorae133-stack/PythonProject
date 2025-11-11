# 반복문
# 정해진 횟수나 조건에 따라
# 특정코드를 반복적으로 실행하도록 만든 문장

# 만일, Hello,World!!를 1번 출력한다면?
# print함수 1번만 사용
print('Hello,World!!')

#그런데, Hello,World!!를 3번 출력한다면 ?
print('Hello,World!!')
print('Hello,World!!')
print('Hello,World!!')

# 만일, 100번 출력해야한다면?- 복붙을 계속할 것인가?
# 단 , 반복시 출력해야 하는 문구각 바뀌면?- 다시 수정- 번거로움!
# 효율적인 반복실행을 위해 반복문을 사용함 !

# ex) 1 ~ 10 까지 출력하기
print(1, end=', ')
print(2, end=', ')
print(3, end=', ')
print(4, end=', ')
print(5, end=', ')
print(6, end=', ')
print(7, end=', ')
print(8, end=', ')
print(9, end=', ')
print(10)

# for 반복
# 정해진 횟수만틈 코드를 반복 실행
#for 반복변수 in range(시작값,종료값-1, 증감값)"
#     반복실행할문장

# range 함수 사용하기 : 정수 시퀀스 생성
print(range(1, 10))
print(list(range(1, 10+1))) # range 객체를 리스트로 변환



# ex) 1 ~ 10 까지 출력하기
for i in range(1, 10+1):
    print(i,end=', ')
print('') # end '' 초기화용 코드


# ex) Hello,World!!를 5번 출력하기
for _ in range(1, 5+1):
    print('Hello,World!!')

# ex) 1 ~ 100 사이 정수 중
#3의 배수지만 ,2의 배수가 아닌 정수 출력
# 또한, 누적합도 계산해서 출력


# 1 ~ 100 사이의 정수 중 조건에 맞는 수 출력 및 누적합 계산

total = 0  # 누적합 저장 변수

print("3의 배수이지만 2의 배수가 아닌 수:")

for i in range(1, 101):
    if i % 3 == 0 and i % 2 != 0:  # 3의 배수이면서 2의 배수가 아닌 경우
        print(i, end=' ')
        total += i  # 누적합 계산

print("\n\n누적합:", total)


for i in range(3, 101,3):
    print(i, end=' ')
print()








# for 문은 유한한 반복을 염두에 두고 설계
# 그래도, 무한루프를 만들고 싶다면 iter 함수 이용

import itertools
for i in itertools.count():
    if i == 9999999:break
    print(i, end=' ')
    i+=1
print()



# for (i = 0; i<= 10; ++1)
