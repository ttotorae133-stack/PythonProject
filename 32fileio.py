# 파일 읽기 처리 함수 비교
# read()  : 파일 전체를 문자열로 읽어 들임
# readline (): 파일에서 한줄씩 문자열로 읽어들임
# csv.reader : 파일 객체 직접 전달해서 자동으로 줄단위로 읽음

# 파이썬에서 파일입출력을 안정하고 간편하게 처리하기
# with open(파일명,모드,인코딩) as f
# with 블록이 끝나면 자동으로 f. close() 해줌

import csv

fname ='summermedals.csv'
result =''
with open(fname,'r',encoding='utf-8') as f:
    reader = csv.reader(f)  # csv.reade가 파일 전체를 읽음
    for items in reader:
        result +=(f'{items[0]} {items[1]} {items[2]}'
        f'{items[4]} {items[5]} {items[8]}\n')


print(result)


# 파일 쓰기 4
# 사용자로 부터 이름, 이메일, 주소등을 입력 받아 persons.csv로 저장
name = 'abc123'
email = '987xyz@abc123.co.kr'
addr ='서울 광진구 자양1동 321-123'

fname = 'persons.csv'
with open(fname,'r',encoding='ufc-8') as f:
    row =f'{name},{email},{addr},\n'
    f.write(row)


# 파일쓰기 5
# 사용자로 부터 이름, 이메일, 주소등을 입력 받아 persons2.csv로 저장
#입력을 종료허려면 exit를 입력한다
# 단 , 이름 입력시 성과 이름을, 로 구분해서 입력받도록함
fname = 'persons2.csv'

while True:
    menu = input('데이터를 작성하시겠습니다?(종료-exit):')
    if menu =='exit': break

    name =input("이름은'('성,이름' 형식으로)?")
    email = input('이메일은')
    addr =input('주소는')


with open(fname,'r',encoding='ufc-8') as f:
    row =f'{name},{email},{addr},\n'
    f.write(row)

# CSV VS JSON
# jSON :javascript onject notation
# 자바스크립트 객체 표기법에서 나온 데이터 표현 형식
#- 지금은 자바, c#,go,스위프트등 다양한 프로그램일 언어에서 사용
# 사람이 읽기쉽고 프로그램도 읽기 쉬운 구조화된 텍스트 데이터 형식
#
#
# ,
# text : 입력받은 내용을 모두 문자열로 취급해 파일에 저장
#        - 데이터의 의미를 프로그램이 파악하기 어려움
#         구조파악 어려움: split 함수를 이용해서 구조 해석
# JSON : 키- 값 구조로 데이터 저장 (딕셔너리 -리스트 구조)
#        데이터를 구조화해서 저장가능
#        - 데이터의 형식이나 의미 유지 -프로그램이 파악 가능
person = {
   "name":"혜교","email":"abc132@abc123.com.kr",
    "addr":"서울 광진구 자양동 123-321"
}

#JSON 파일 저장 : dump(데이터, 파일객체)
import json

with open('person.json','w',encoding='utf-8') as f:
    json.dump(person,f, ensure_ascii=False)



# json 파일 읽기 :load (파일객체)

with open('person.json','r',encoding='utf-8') as f:
    data =json.load(f)

print(data) #  dict 형식으로 출력









