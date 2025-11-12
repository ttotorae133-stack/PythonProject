# 21 - 반복 cnrk

while True:
    ismarried = input("결혼 여부를 입력하세요 (예/아니오): ")
    salary = int(input("연봉을 입력하세요 (원): "))

    if ismarried == "아니오":
        # 미혼인 경우
        if salary < 30000000:
            tax_rate = 0.10  # 10%
        else:
            tax_rate = 0.25  # 25%
    elif ismarried == "예":
        # 결혼한 경우
        if salary < 60000000:
            tax_rate = 0.10  # 10%
        else:
            tax_rate = 0.25  # 25%
    else:
        print(" 결혼 여부 입력이 잘못되었습니다. '예' 또는 '아니오'로 입력해주세요.")
        continue

    # 세금 계산
    tax = salary * tax_rate

    # 결과 출력
    print(f"납부해야 할 세금은: {tax:,.0f} 원입니다.")

    # 계속 여부
    cont = input("계속하시겠습니까? (y/n): ").lower()
    if cont == 'n':
        print("프로그램을 종료합니다.")
        break








# 23 -중첩

# 26 반복 추가 2


# 30