# continye와 break
# 반복의 흐름을 제어할떄 주로 사용하는 명령
# break : 반복 진행 중, 조건에 따라 반복 중지시 사용
# continue : 반복 진행중, 조건에 따라 반복을 건너뛰고 싶을떄 사용

# ex) 1 ~ 1000까지 3의 배수의 총합을 구하라
# 단, 총합이 1000을 넘으면 중단하고 결과 출력
sum=0

#for i in range(1,1000+1,):
for i in range(1, 1000 + 1, 3):
    if sum >= 50000: break
    print(sum, i)

    sum += i

print(sum, i)


# ex) 1 ~ 1000까지 3의 배수의 총합을 구하라
# 단, 2의 배수는 제외한다
sum=0
for i in range(3, 1000 + 1, 3):
    print(f'{i} - {sum}')
    if sum >= 50000: break
    if i % 2 == 0: continue # 2배수라면 반복 건너뜀, 추천 !
    sum += i

print(f'최종 : {i} - {sum}')
# 또한, 총합이 1000을 넘으면 중단하고 결과 출력
