# 21
# 사용자 입력 받기
salary = int(input("연봉을 입력하세요 (단위: 원): "))
ismarried = input("결혼 여부를 입력하세요 (예/아니오): ")

# 결혼 여부에 따른 세금 규칙
if  ismarried == "아니오":
    # 미혼인 경우
    if salary < 30000000:
        tax_rate = 0.10  # 10% 할인
    else:
        tax_rate = 0.25  # 25% 할인
elif ismarried == "예":
    # 결혼한 경우
    if salary < 60000000:
        tax_rate = 0.10  # 10% 할인
    else:
        tax_rate = 0.25  # 25% 할인
else:
    print("결혼 여부 입력이 잘못되었습니다.")
    exit()

# 세금 계산
tax = salary * tax_rate

# 결과 출력
print(f"납부해야 할 세금은: {tax:,.0f} 원입니다.")


# 23

# 26

# 31

# 32