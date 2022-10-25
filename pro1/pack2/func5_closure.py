# 클로저(closure) : scope에 제약을 받지않는 변수를 포함하고 있는 코드 블록이다. //  https://cafe.daum.net/flowlife/RUrO/31 / 참고
# 내부함수의 주소를 반환함으로 해서 함수 내의 지역변수를 함수 밖에서 참조 가능

def funcTimes(a, b): 
    c = a * b
    return c

print(funcTimes(2, 3))

kbs = funcTimes(2, 3)
print(kbs)
kbs = funcTimes
print(kbs)
print(kbs(2, 3))
print(id(kbs), id(funcTimes))

del funcTimes
# funcTimes()
print(kbs(2, 3))

mbc = sbs = kbs
print(mbc(2, 3))
# ---------------------------
print('클로저를 사용하지 않은 경우 ---')
# count = 0
def out():
    count = 0
    def inn():
        nonlocal count # nonlocal -  지역변수로 바꿔준다.
        count += 1 # 지역변수는 안에서만 누적이 된다.
        # ...
        return count
    # print(inn())
    imsi = inn()
    return imsi

# print(out())
# print(count) # err 글로벌지역변수가 아니기때문에 에러발생
# out()
# out()
print(out())
print(out())

print('\n클로저를 사용한 경우 ---')
def outer():
    count = 0
    def inner():
        nonlocal count  # nonlocal -  지역변수로 바꿔준다.
        count += 1  # 지역변수는 안에서만 누적이 된다.
        # ...
        return count
    return inner    # < === 요게 클로저 : 내부함수의 주소를 반환

var1 = outer()  # inner의 주소를 받고 있다.
print(var1)
print(var1())
print(var1())   # inner에서의 count를 참조하면서 누적이 된다.
print(var1())

print('*** 수량 * 단가 * 세금을 계산하는 함수 만들기')
# 분기별로 세금은 동적이다.
def outer2(tax):    # 함수안에서 선언했기때문에 local(지역변수)이다.
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2   # 주소를 리턴 하는것 // (inner2() 결과를 리턴하는것)

# 1분기에는 tax가 0.1 부과
q1 = outer2(0.1)
result1 = q1(5, 50000)
print('result1 : ', result1)
result2 = q1(1, 10000)
print('result2 : ', result2)

# 2분기에는 tax가 0.05 부과
q2 = outer2(0.05)
result3 = q2(5, 50000)
print('result3 : ', result3)
result4 = q2(1, 10000)
print('result4 : ', result4)


    


