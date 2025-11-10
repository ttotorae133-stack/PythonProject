# 23 복권 - 반복문으로 재작성
import random

print("=== 복권 추첨 프로그램 ===")

# A. 사용자로부터 복권 숫자 3자리 입력 받기
user = input("복권 숫자 3자리를 입력하세요 (예: 123): ")

# B. 프로그램에서 난수 생성
lotto = str(random.randint(100, 999))

print(f"당첨 번호는 {lotto} 입니다!")

# C~E. 일치 개수 계산
match = 0
for digit in user:
    if digit in lotto:
        match += 1

# 결과 판정 (0개 일치는 출력하지 않음)
if match == 3:
    print("일치한 숫자 개수: 3개 → 상금 1,000,000원 지급!")
elif match == 2:
    print("일치한 숫자 개수: 2개 → 상금 10,000원 지급!")
elif match == 1:
    print("일치한 숫자 개수: 1개 → 상금 1,000원 지급!")
# match == 0이면 아무것도 출력하지 않음



# 24 구구단- 반복문으로 재작성
# 구구단 출력 (for문 버전)

dan = int(input("출력을 원하는 단을 입력: "))

print(f"*** {dan} 단 ***")
for i in range(1, 10):
    print(f"{dan} * {i} = {dan * i}")

# 구구단 출력 (while문 버전)

dan = int(input("출력을 원하는 단을 입력: "))

print(f"*** {dan} 단 ***")
i = 1
while i <= 9:
    print(f"{dan} * {i} = {dan * i}")
    i += 1









# 26 숫자 맞추기 -반복문 추가
import random

import random

print("=== 숫자 맞추기 게임 ===")

# b. 컴퓨터는 임의의 숫자 생성
num2 = random.randint(1, 100)

while True:
    # a. 사용자 입력
    num1 = int(input("1~100 사이의 숫자를 입력하세요: "))

    # c. num1 > num2
    if num1 > num2:
        print("추측한 숫자가 큽니다.")
    # d. num1 < num2
    elif num1 < num2:
        print("추측한 숫자가 작습니다.")
    # e. num1 == num2
    else:
        print(f"빙고! 숫자를 맞췄습니다! 정답은 {num2}입니다 🎯")
        break  # 프로그램 종료


# 30 구구단 테이블 -반복문으로 재작성

# 32 주민번호 검사 - 반복문으로 재작성