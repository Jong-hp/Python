# 일급함수 : 함수안에 함수, 인자로 함수 전달, 반환값이 함수    // https://hjaem.info/articles/kr_4_1 / 참고
def func1(a, b):
    return a + b

func2 = func1
print(func1(3, 4))
print(func2(3, 4))

print()
def func3(func):    # 가인수로 함수 수신
    def func4():
        print('나는 내부함수야~')
    func4()
    return func     # 반환값이 함수

mbc = func3(func1)  # 실인수로 함수 전달
print(id(func1))
print(id(mbc))
print(mbc(3, 4))

print('Lambda : 축약함수, 이름이 없는 한 줄 짜리 함수')
# 형식 : lambda 인자, ...:표현식    return문 없이 결과 반환 (일회성)
# def를 쓸 정도로 복잡하지 않거나 , def를 적용할 수 없는 곳애 사용하면 효과적

def Hap(x, y):
    return x + y

print(Hap(1, 2))

print((lambda x, y:x + y)(1, 2))


g = lambda x, y:x + y
print(g)
print(g(3, 4))

kbs = lambda a, su=10:a + su
print(kbs(5))
print(kbs(5, 6))

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1,2,3,m=4,n=5)

print()
li = [lambda a, b:a + b, lambda a:a + 5]
print(li[0](3, 4))
print(li[1](3))

print('어떤 함수의 인자로 람다를 사용 ---')  # https://www.daleseo.com/python-filter / 참고
# filter(함수, 집합형자료)
print(list(filter(lambda a: a < 5, range(10))))
print(list(filter(lambda a: a % 2, range(10)))) # True 만 찍혀서 홀수만 나옴 // (0 = false 이기 때문에 출력되지 않음)

# 1 ~ 100 사이의 정수 중 5의 배수이거나 7의 배수만 걸러서 출력
print(list(filter(lambda a: a % 5 == 0 or a % 7 == 0, range(1, 101))))




