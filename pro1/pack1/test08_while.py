# 반복문 while
# while 조건: ~

a = 1
while a <= 5:
    print(a, end = ' ')
    a += 1
    
print('while 수행 후 %d'%a)
    
print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i:' + str(i) + ', j:' + str(j))
        j = j + 1
    i += 1
    
print('1 ~ 100 사이의 정수 중 3의 배수의 합 출력')
i = 0; hap = 0
while i < 100:
    if i % 3 == 0:
        # print(i, end = ' ')
        hap += i
    i += 1
    # print(i, end = ' ')
    
print(' 합은 {}'.format(hap))

print()
colors= ['r', 'g', 'b']
print(colors[0])
a = 0
while a < len(colors):
    print(colors[a],end = ' ')
    a += 1
    
print()

while colors:
    print(colors.pop(0), end = ' ')
    # print(len(colors))
    
print()
i = 1
while i <= 10:
    j = 1
    re = ''
    while j <= i:
        re = re + '*'
        j += 1
    print(re)
    i += 1
    
print('-------------------')
import time
# time.sleep(3)
sw = input('폭탄 스위치를 누를까요?[y/n]')
if sw == 'Y' or sw == 'y':
    count = 5
    while 1 <= count:
        print('%d 초 남았습니다.'%count)
        time.sleep(1)
        count -= 1
    print('폭팔 ~~~')
        
elif sw == 'N' or sw == 'n':
    print('작업 취소')
else:
    print('y 또는 n을 누르시오')
print('end')

    
    
    
    
    
    
    