# 변수의 생존 범위 (scope rule)
# 변수 접근 순서 : Local > Enclosing function > Global

player = '전국대표' # 전역변수

def funcSoccer():
    name = '신기해'    # 지역변수
    player = '지역대표'
    print(name, player)

funcSoccer()
# print(name)
print(player)

print('----------')
a=10; b=20; c=30
print('1) a:{}, b:{}, c:{}'.format(a, b, c))

def func1():
    a = 40
    b = 50
    c = 100
    def func2():
        # c = 60
        func2_local = 7
        global c # 많이쓰임
        nonlocal b
        print('2) a:{}, b:{}, c:{}'.format(a, b, c))
        c = 60  # local variable 'c' referenced before assignment
        b = 70
        
    func2()
    print('3) a:{}, b:{}, c:{}'.format(a, b, c))
    
func1()
print('함수 수행 후) a:{}, b:{}, c:{}'.format(a, b, c))
