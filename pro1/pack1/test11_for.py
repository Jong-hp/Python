# for + range 수혈을 생성해주는 함수
from debugpy.common.json import object
print(list(range(1, 6, 1)))
print(set(range(1, 6)))
print(tuple(range(1, 6)))
print(list(range(1, 11, 2)))
print(list(range(6)))
print(list(range(0, 6, 1)))
print(list(range(-10, -100, -20)))

print()
for i in range(6):
    print(i, end = ' ')
print()

for _ in range(6):
    print('안녕', end = ' ')
    # pass 아무것도 없다.
print()

print()
for i in range(1, 10):
    print('{0}*{1}={2}'.format(2, i, 2 * i), end = ' ')
print()

print()
tot = 0
for i in range(1, 11):
    tot += i
    
print('합은 ' + str(tot))
print('합은 ', sum(range(1, 11))) # sum 내장함수

# 문 1) 2 ~ 9 단 까지 출력
for i in range(2, 10):
    for j in range(1,10):
        print('{0}*{1}={2}'.format( i, j, i * j), end = ' ')
print()
# 문 2) 1 ~ 100 사이의 3의 배수이면서 5의 배수의 합 출력
tot = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        tot += i
print('합은 ', tot)

# 문 3) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 두 수 출력
# 출력 예) 1 3
#        2 2
#        ...
for i in range(1, 7):
    for j in range(1, 7):
        su = i + j
        if su % 4 == 0:
            print(i, j)
            
print()
# n-gram : 문자열에서 N개의 연속된 요소를 추출하는 방법
text = 'hello'

for i in range(len(text) - 1):
    print(text[i:i + 2])

