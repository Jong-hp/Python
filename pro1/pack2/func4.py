# 함수 : argument와 parameter 키워드로 matching 하기
# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 인수와 매개변수를 동일이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우
# https://webroadcast.tistory.com/41 참고(argument와 parameter 차이)

def showGugu(start, end=5): # 파라미터와 아규먼트의 갯수는 같아야 오류가 안남
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
    

showGugu(2, 3)  # 위치 매개변수
print()
showGugu(3) # 기본값 매개변수
print()
showGugu(start=2, end=3)    # 키워드 매개변수
print()
showGugu(end=3, start=2)    # 키워드 매개변수
print()
showGugu(2, end=3)  # 키워드 매개변수
print()
#    showGugu(start=2, 3)   # SyntaxError: positional argument follows keyword argument
#    showGugu(end=3, 2)   # SyntaxError: positional argument follows keyword argument

print('\n가변인수 처리')
def func1(*ar): # 동적처리할땐 *
    # print(ar)
    for i in ar:
        print('밥 : ' + i)
    print()

print()
func1('비빔밥', '공기밥')
func1('비빔밥', '공기밥', '김밥')

print()
def func2(a, *ar): # 동적처리할땐 *
#    def func2(*ar, a): # 동적처리할땐 * 패킹 연산자는 무조건 뒤로
    print(a)
    for i in ar:
        print('밥 : ' + i)
    print()

func2('비빔밥', '공기밥')
func2('비빔밥', '공기밥', '김밥')

print()
def calcProcess(op, *ar):
    if op == 'sum':
        re = 0
        for i in ar:
            re += i
    elif op == 'mul':
        re = 1
        for i in ar:
            re *= i
    return re

print(calcProcess('sum', 1,2,3,4,5)) # tuple
print(calcProcess('mul', 1,2,3,4,5))
print(calcProcess('mul', 1,2,3,4,5,1,2,3,4,5))

print()
def func3(w, h, **other):
    print('w:{}, h:{}'.format(w, h))
    print(other)
    
func3(55, 160)
func3(55, 160, irum='홍길동')
# func3(55, 160, {'irum'='홍길동'}) # err
func3(55, 160, irum='홍길동', nai=23)

print()
def func4(a, b, *c, **d):
    print(a, b)
    print(c)
    print(d)
    
func4(1, 2)
func4(1, 2, 3)
func4(1, 2, 3, 4, 5)
func4(1, 2, 3, 4, 5, x=6, y=7)




