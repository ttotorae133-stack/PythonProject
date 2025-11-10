# 35 -거스름돈 계산
# 지불할 금액: 32100
# 지불한 금액 : 50000
# 거스름돈 : 17900

product = 32100
pay = 50000
charge = pay -product

print(f'물건가격 : {product},지불금액 : {pay},'f'거스름돈 :{charge}')

n50000 = int(charge / 500000)
print('50000원:',(n50000,'개')
charge = charge - (50000 * n50000)

n10000 = int(charge / 10000)
print('10000원:', (n10000),'개')
charge = charge -( 10000 * n10000)

n5000 = int(charge / 5000)
print ('5000원:', (n5000),'개')





# 잔돈 계산
n50000 = charge //50000
charge = charge % 50000






#문자열 비교 - 문자열 pool



