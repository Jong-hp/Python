# 반복문 continue, break

a = 0

while a < 10:
    a += 1
    if a == 3:continue
    if a == 5:break
    print(a)
else:
    print('while문 정상 수행')
    
print('while 수행 후 %d'%a)

print()
# 난수 발생
import random
# random.seed(42) # 고정된 값으로 나옴
num = random.randint(1, 10) # 랜덤으로 나옴
# print(num)
# while True:
#     print('1 ~ 10 사이의 컴이 가진 예상 숫자 입력:')
#     guess = int(input())
#     if guess == num:
#         print('성공' * 10)
#         break
#     elif guess < num:
#         print('더 큰 수 입력')
#     elif guess > num:
#         print('더 작은 수 입력')
                
    
# 의사 난수(pseudo random)
friend = ['tom', 'john', 'oscar']
print(friend)
print(random.choice(friend)) # 3개 중 하나 랜덤
print(random.sample(friend, 3)) # 3개를 전부 랜덤
random.shuffle(friend)
print(friend)

