# 21 - 함수로 재작성 : computeTax
from yeahue.examples_libv1 import compute_tax

while True:
    salary = int(input('연봉을 입력하세요(만원 단위): '))
    isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()

    rate, tax = compute_tax(isMarried, salary)

    result = f'''
    적용세율 : {rate}%
    납부해야 할 세금은 {tax}만원입니다
    '''

    print(result)
    cont = input('계속하시겠습니까? (y/n)').lower()
    if cont == 'n': break


# 23 - 함수로 재작성 : lotto999
def count_matches(match):
    for i in range(3):
        for j in range(3):
            if lotto[i] == mykey[j]: match += 1



import random

lotto = str(random.randint(123, 789))
mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
prize = 0

match = count_matches(mykey,lotto)
match = 0   # 일치수


if match == 3: prize = 1000000
elif match == 2: prize = 10000
elif match == 1: prize = 1000

result = f'''
# 당첨번호 : {lotto}
# 당신의 복권번호 : {mykey}
# 일치한 숫자 갯수 : {match}
# 당첨 금액 : {prize}원
# '''
print(result)


# 24 - 함수로 재작성 : gugudan
def generate_gugudan(dan):
    """
    단을 입력받아 구구단 출력하는 함수
    :param d
    """
    if 1 <= dan <= 9:
        result = f'=== {dan}단 ===\n'
        for i in range(1, 9+1):
            result += f'{dan} x {i} = {dan * i}'
    else:
        result = ""

    return result

dan = int(input('출력할 구구단 단수를 입력하세여 (1-9:'))

result = generate_gugudan(dan)

print(result)










# 32 - 함수로 재작성 : checkJumin

jumin = '450124-1234590'
sum = 0

# a, b
code = []
for i in range(13):
 if jumin[i].isdigit():
     code.append(int(jumin[i]))
for j in jumin:
 if j.isdigit():
     code.append(int(j))
code = [int(j) for j in jumin if j.isdigit()]

print(f'추출된 주민번호 : {code}')

wght = [2,3,4,5,6,7,8,9,2,3,4,5]
wght = []
for i in range(12):
 wght.append((i % 8) + 2)
wght = [(i % 8) + 2 for i in range(12)]

print(f'자동생성된 가중치 : {wght}')

for i in range(12):
    sum += code[i] * wght[i]

print(sum)

# c,
checker = 11 - (sum % 11)
print(checker, str(checker)[-1] == jumin[13])













