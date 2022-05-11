#문자열 출력
print("#문자열 출력")
print("""life is too short, you need python""");print("life is too short, you need python")
print('life is too short, you need python');print('''life is too short, you need python''')
print()
#문자열에 작은 따옴표가 있을 경우
print("#문자열에 작은 따옴표가 있을 경우")
print("python's food")
print()
#문자열에 큰 따옴표 있을 경우 \ 사용 또는 ' 사용
print("#문자열에 큰 따옴표 있을 경우 \ 사용 또는 ' 사용")
print("\"python is very easy.\"he says.")
a = "그는 \"파이썬은 매우 쉽다\"라고 말했다."
print(a)
print('"python is very easy."he says."')
print()
#줄바꿈 \n, ''', """ 사용
print("#줄바꿈")
print("life is too short\nYou need python")#\n은 읽기에 불편하고 줄이 길어지느 단점이 있음
multiline = '''
인생은 
너무 짧다
'''
multiline2 = """
너는 파이썬이
필요하다.
"""

print(multiline)
print(multiline2)

#문자열 연산하기
print("#문자열 연산하기")
head = "python"
tail = " is fun"
print(head + tail)
print(head*2 + tail*2)
print("=" * 50)

print()
#문자열 길이 구하기
print("#문자열 길이 구하기")
a = "life is too short"
print(len(a))

print()
#문자열 인덱싱
print("#문자열 인덱싱")
a = "life is too short, You need python"
# l=0 i=1 f=2 ~> o = 10 "파이썬은 0부터 숫자를 센다"
print(a[0]+a[10]+a[12]+a[3]+a[15])
# [-1]은 뒤에서 부터
print(a[-1],a[-2],a[-3])

print()
# 문자열 슬라이싱 미사용
print("#문자열 슬라이싱")
a = "life is too short, You need python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
# 문자열 슬라이싱 사용
print(a[0:4],a[5:8])
print(a[19:]);print(a[:19])
# 슬라이싱으로 문자열 나누기
a = "20220426Rainy"
date = a[:8]
weather = a[8:]
print(weather, date)
year = a[0:4]
day = a[4:8]
print(day, year) # 인덱싱과 슬라이싱은 매우 자주 사용

print()
#pithon이라는 문장을 python으로 바꾸기
print("#pithon이라는 문장을 python으로 바꾸기")
a = "pithon"
print(a)
# a[1] = 'y' 이러면 오류나옴!
print(a[:1]+"y"+a[2:])

print()
#문자열 포매팅
print("#문자열 포매팅")
print("현재온도는 %d 입니다." %3)
print("현재온도는 %s 입니다." %"오도")
temp = 11
print("현재온도는 %a 입니다." %temp)
#2개 이상 값 넣기
number =10
day = "three"
print("i ate %d apples. So I was sick for %s days." %(number, day))
#오류 print("I ate %d apples. so I was sick for %s days.") %(number, day)

#포매팅 연산자 %d와 %를 같이 쓸 떄는 %%를 쓴다.
#오류 print("error is %d%." %98)
print("error is %d%%." %98)
#교재 60페이지