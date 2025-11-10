# 22 - 윤년leap year
# 1년은 365일이지만, 실제는 365.24일
# 이러한 오차를 보정하기 위해
# 4년에 한번씩 2월을 29일까지 둠 (평년에는 28일)
# 판정기준
# a: 현재 연도가 4로 나눠 떨어지지만, 100으로느 나눠  떨어지지않음
# b : 그중에서도 400으로 나눠 떨어지면
# 2024,2000 :윤년
year = 2000
result = '윤년' if ((year % 4 == 0)) and (year % 100 != 0)
               or (year % 400 == 0)) else '평년'
print(result)

#파이썬 표준라이브러리를 사용하면 편하게 코드 작성 가능
import calendar
print(calendar.isleap(2024))
print(calendar.isleap(2025))
