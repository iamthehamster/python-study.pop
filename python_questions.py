print("Hello World")

print("Mary's cosmetics")

print('신씨가 소리질렀다. "도둑이야".')

print("C:\Windows")

print("안녕하세요. \n만나서\t\t반갑습니다.")
#\n은 줄바꾸기, \t는 tab의 역할.

print("naver;kakao;sk;smasung")

print("first", end="");print("second")
#end""는 줄바뀜 없음, sep""는 띄어쓰기 없음
#end"~"의 ~에 들어가는 내용은 마지막에 프린트
#sep"~"의 ~에 들어가는 내용은 중간중간에 프린트

print(5/3)

삼성전자 = 50000
총_평가금액 = 삼성전자*10
print(총_평가금액)

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
#type()은 데이터의 종류를 판별. ex) int, float

s = "hello"
t = "python"
print(s+"!"+t)
#중간에 다른 문자를 넣고 싶을때는 string 처리 필요

a = "132"
print(type(a))
#type()의 결괏값을 띄우고 싶을때도 print 사용

num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))
#문자열을 정수로 변환할 때 int()사용

num = 100
result = str(num)
print(result, type(result))
#정수를 문자열을 변환할 때 result = str(num)

a = float("15.79")
print(a, type(a))
#문자열을 실수로 변환할 때 data 값 정한 후 float(data) 후 다른 형변환과 같이 print(data, (type())처리

year = "2024"
print(int(year)-1)
print(int(year)-2)
print(int(year)-3)
#문자열 타입의 연도를 정수로 변환, 최근 3개년 정수 형태로 print

할부금액 = 48584
할부개월 = 36
총금액 = (할부금액*할부개월)
print(총금액)

letters = "python"
print(letters[0], letters[2])
#문자열 인덱싱 [], 처음은 0으로 시작

license_plate = "24가 2210"
print(license_plate[4:8])
#문자열 슬라이싱: string[start:end] 기본적 슬라이싱, string[start:end:step] 기본 슬라이싱에 간격(step) 추가

string = "홀짝홀짝홀짝"
print(string[::2])

string = "PYTHON"
print(string[::-1])
#문자열 슬라이싱 응용: 거꾸로 입력 - step을 -1로 입력

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
#문자열 치환: .replace("", "")

phone_number = "010-1111-2222"
phone_number2 = phone_number.replace("-", "")
print(phone_number2)

lang = "python"
#lang[0] = "P"
print(lang)
#문자열은 수정 불가. line92에서 문자열 python의 첫번째 글자를 정의하려고 시도. 이것도 불가

string = "abcdefe2a354a32a"
string1 = string.replace("a", "A")
print(string1)

t1 = "python"
t2 = "java"
print((t1+" "+t2+" ")*4)

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))
# %formatting: %s - string, %d - int, %(,) - given detail

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
#format(): inside {}, number,string,and can be empty. if empty, value inside .format() should go inside sequentially

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
#f-string: same as %, format(), but simple. just put f infront of "", same {} used for inner value.

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
result = int(컴마제거)
print(result, type(result))

분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])
#string slicing: sliced from start to B-1 of [A:B]

data = " 삼성전자 "
data1 = data.strip()
print(data1)
#strip(): 공백제거 - lstrip: 왼쪽 공백, rstrip: 오른쪽 공백 제거

#diverse methods: .upper: 문자열을 대문자로 / .lower: 문자열을 소문자로 / .capitalize: 문자열의 첫글자를 대문자로 / .endswith: 파일 이름이 ~으로 끝나는지 / .startswith: 파일 이름이 ~으로 시작하는지 / .split(): 문자열에서 공백을 기준으로 분리 / .split(~): 문자열에서 ~을 기준으로 분리

