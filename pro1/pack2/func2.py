# 함수 만들기
# def 함수명(매개변수,...): ~

print('뭔가를 하다가...')

def DoFunc1():  # 함수의 생성
    print('DoFunc1 수행')
    # return None # 생략

print('뭔가를 하다가 2...')
DoFunc1()   # 함수 호출
print('뭔가를 하다가 2...')
DoFunc1()
print(DoFunc1)
DoFunc2 = DoFunc1   # 주소 치환
DoFunc2()
print(DoFunc1())

print()
def doFunc3(para1, para2):
    # pass
    result = para1 + para2
    # print(result)
    return result

print(doFunc3(10, 20))
aa = doFunc3(10, 20)
print(aa)
print(id(doFunc3),doFunc3,doFunc3(1, 2))
print('현재 파일(모듈)이 사용 중인 객체 목록 : ', globals())

print(doFunc3('대한', '민국'))
# print(doFunc3('대한', 1))    # TypeError
# print(doFunc3(1)) # missing 1 required positional argument
# print(doFunc3(1, 2, 3)) # takes 2 positional arguments but 3 were given

print('-----------')
def doFunc4(arg1, arg2):
    if (arg1 + arg2) % 2 == 1:
        return
    else:
        aa = doFunc5(arg1, arg2) # 함수 내에서 다른 함수 호출
        print(aa)

def doFunc5(arg1, arg2):
    return arg1 + arg2

doFunc4(5, 6)
doFunc4(5, 5)

print()
def swapfunc(a, b):
    return b, a # tuple type 으로 묶여 하나의 값으로 반환
    # return (b, a)
    # return [b, a] # list type

a = 10; b = 20
print(swapfunc(a, b))

print() # 내부함수
def func1():
    print('func1 함수 맴버')
    def func2():
        print('func1의 내부 함수인 func2 맴버')
    func2()

func1()

print()
# if 조건식 안에 함수 사용
def isOdd(para):
    return para % 2 == 1

print(isOdd(5))
print(isOdd(6))
mydict = {x:x*x for x in range(11) if isOdd(x)}
print(mydict)


print('함수연습용 게임 ---')
import random
import time

def gameSijak():
    print('보물을 찾아 여행을 떠나자. 동굴 문은 두 개다.')
    print('동굴 속에는 착한 용과 무서운 용이 있다.')
    print('랜덤하게 동굴을 선택해 착한 용을 만나면 보물을 획득, 나쁜 용을 만나면 황천길')
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('동굴을 선택(1 또는 2)')
        cave = input()
    return cave

def chkCave(selectNum):
    print('동굴에 도착')
    time.sleep(3)
    rndNum = random.randint(1, 2)
    
    if selectNum == str(rndNum):
        print('와우 착한용을 만나 보물을 얻어 행복하게 삶')
    else:
        print('그 후 그를 본 사람은 아무도 없었다.')

playAgain = 'y'
while playAgain == 'y':
    gameSijak()
    caveNumber = chooseCave()
    chkCave(caveNumber)
    print('계속할까요?(y or n)')
    playAgain = input()