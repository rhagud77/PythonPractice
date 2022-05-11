# Q1. 다음 코드의 결괏값은 무엇일까? shirt
a = "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# Q2. While문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자. #166833 출력
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0 :
        result += i
        print(result)
    i += 1
print(result)

# Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
i = 0
while True:
    i += 1
    if i > 5 : break
    print(i*"*")

# Q4. for문을 사용해 1부터 100까지의 숫자를 출력해보자.
for i in range(1,101):
    print(i)

# Q5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
print(total)
average = total/10
print(average)
