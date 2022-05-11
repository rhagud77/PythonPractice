#포맷 코드와 숫자 함께 사용하기 p60
print("정렬과 공백")
print("%10s" % "hi") #전체 길이 10개인 문자열 공간에서 오른쪽 정렬
print("%-10sjane" %'hi') #-10은 왼쪽 정렬
print("%-10sthis is minesadfdsfdsfadfsafdf" %'hihih')

print()
#소수점 표현하기
print("소수점 표현하기")
print("%0.4f" % 3.42134234) #소수점 네 번째 자리까지 나타내기
print("%10.4f" % 3.42134234) #소수점 네 번째 자리까지 표시하고 전체 길이 10개인 문자열 공간에서 오른쪽 정렬

print()
#숫자 바로 대입하기
print("I eat {0} apples". format(3))
print("I eat {0} apples". format("five"))
number = 3
print("I eat {0} apples". format(number))
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days")