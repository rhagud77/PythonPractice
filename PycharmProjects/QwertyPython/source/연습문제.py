#Q1 홍길동 씨의 과목별 점수는 다음과 같다. 평균 점수를 구해 보자.
국어=80
영어=75
수학=55
print((국어+영어+수학)/3)

점수 = {'국어':80, '영어':75, '수학':55}
average = sum(점수.values()) / len(점수)
print(average)

print()
#02 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
if 13%2 == 1:
    print("홀수")
else:
    print("짝수")

a = 13%2
if a == 1:
    print("홀수")
else:
    print("짝수")

def check(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
check(22)

print()
#03 홍길동 씨의 주민번호는 881120-1068234이다.
pin = "881120-1068234"
yyyymmdd = "19"+pin[:6]
print(yyyymmdd)
num = pin[7:]
print(num)
#

print()
#Q4 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.
pin = "881120-1068234"
print(pin[7])

a = pin[7]
if a == "1":
    print("man")
else:
    print("woman")
#문자열 인덱싱

print()
#Q5 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
print(a[:3]+"#"+a[4:])
#문자열 관련 replace함수 p70

print()
#Q6 [1,3,5,3,2] 리스트를 [5,4,3,2,1]로 만들어 보자.
a = [1, 3, 5, 4, 2]
a.sort() #p80 리스트 정렬
print(a)
a.reverse() #p81 리스트 뒤집기
print(a)

#07 ['Life', 'is', 'too', 'short'] 리스트를 life is too short 문자열로 만들어 출력해 보자.
a = ['life', 'is', 'too', 'short']
print(a[0]+" "+a[1]+" "+a[2]+" "+a[3])

resurt = " ".join(a) #문자열 삽입 join함수 p68
print(resurt)

a = "Life is too short" #문자열 나누기 split함수 p70
print(a.split())

#08 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
a = (1, 2, 3)
print(a + (4, )) # 튜플에 값 넣기 p

a = (1, 2, 3)
b = (4, )
print(a + b) # 튜플에 값 넣기2 p

a = [1, 2, 3]
a.append(4) # 리스트에 값 넣기 p
print(a)
