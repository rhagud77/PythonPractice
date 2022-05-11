########### IF문 ############
print("-IF문-")
print()
# 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다. p.117
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# 들여쓰기 주의
money = True
if money:
    print("택시를");print("타고")
    print("가라")
# 조건문 다음에 콜론(:) 잊지 말기 앞으로 배울 while, for, def, class문에서도 같음
x = 3
y = 2
if x > y:
    print("True")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# and, or, not p123
money = 2000
card = 2000
if money >= 3000 or card >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if money + card >= 5000:
    print("택시")
else:
    print("도보")
# in, not in p.124
print()
x = 5
if x in [1, 2, 3]:
    print("x은 1,2,3 안에 있다")
else:
    print("%x는 1,2,3 안에 없다" %x)
# in 예제
# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
print()
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# 주머니에 카드가 없다면 걸어가고 있다면 버스를 타고 가라는 문장을 조건문으로 만들어 보자.
pocket = ['paper', 'cellphone', 'money', 'card']
if 'card' in pocket:
    print("버스를 타고 가라")
else:
    print("걸어가라")

# elif문 p.126
pocket = ['paper', 'cellphone']
card = False
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# if문을 한 줄로 작성하기
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: print("돈이 있다")
else: print("카드를 꺼내라")
# 조건부 표현식
score = 50
if score >= 60:
    message = "sucess"
    print(message)
else:
    message = "failure"
    print(message)
######################################