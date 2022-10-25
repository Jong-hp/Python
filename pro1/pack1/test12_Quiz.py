# while / if 연습문제
# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력

i = hap = 0

while i <= 100:
    i += 1
    if i % 3 == 0 and i % 2 != 0:
        print(i, end = ' ')
        hap += i
    
print(' 합은 {}'.format(hap))

# 문2) 2 ~ 5 까지의 구구단 출력

i = 1
while i < 5:
    i = i + 1
    j = 1
    while j < 10:
        print(i, 'X', j, '=', i*j)
        j = j + 1
        
#문3)  -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력

x = -1; y = 3; sum = 0

while y<=99:
    z = x + y
    x -= 4
    y += 4
    sum += z
    
print(str(sum))


i=1; sum=0
while i<=25:
    x=-4*i+3
    y=4*i-1
    z=x+y
    sum+=z
    i+=1

print(str(sum))


#문4)  1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력




