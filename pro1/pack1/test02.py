# 연산자 출력 서식

v1 = 2 # 치환
v1 = v2 = v3 = v4 = 5
print(v1, v2, v3, v4)
v1 = 1, 2, 3
print(v1)
v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당 packing')
# v1, *v2 = 1,2,3,4,5
*v1, v2 = 1,2,3,4,5
# *v1, *v2 = 1,2,3,4,5  # err
print(v1)
print(v2)


v1, v2, *v3 = 1,2,3,4,5
print(v1, v2, v3)

print()
print('-------------')
print('\n연산자(산술, 관계, 논리)')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3)
print(5 // 5, 5 % 3, divmod(5, 3))

print('연산자 우선순위', 3 + 4 * 5, (3 + 4) * 5)
# 소괄호 () > 산술연산자(** > *, / > +, -) > 관리연산자 > 논리연산자 > 치환(=)

print('관계연산자')
print(5 > 3, 5 == 3, 5 != 3)
print('논리연산자')
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))

print('문자열 더하기 연산자')
print('파이썬' + '만' + "세")
print('파이썬' * 20)

print('누적')
a = 10
a = a + 1
a += 1
# a++ # 증감 연산자 X a--
print('a:', a)

print()
print(a, a * -1, -a, --a)

print('bool : ', True, False, type(True))
print(bool(True), bool(1), bool(-23.4), bool('kbs')) # 구체적인 값을 가지고 있으면 True
print(bool(False), bool(0), bool(0.0), bool(''), bool(None), bool([]), bool(()), bool({})) # 구체적인 값이 없으면 False

print('***' * 10)
#출력 서식
print(format(123.45678, '10.3f'))
print(format(123.45678, '10.3'))
print(format(123, '10d'))
print ('{0:.3f}'.format(1.0/3))
print ('{0:_^11}'.format('hello'))
print ('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print('이름:{0}, 가격:{1}'.format('마우스', 5000))
print('이름:{}, 가격:{}'.format('마우스', 5000))
print('이름:{1}, 가격:{0}'.format('마우스', 5000))
print('이름:{1}, 가격:{0} 가격:{0}'.format('마우스', 5000)) # 제일 많이 쓰는 방법

print('나는 나이가 %d 이다.'%23) # 정수
print('나는 나이가 %s 이다.'%'스물셋') # 스트링
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동')) 
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100)) # 실수

print('~~~' * 10)
print('aa\tbb') # \t tap키
print(r'aa\tbb') # raw string을 선행하면 이스케이프 기능 해제
print("c:\aa\bbc\nbc.txt")
print(r"c:\aa\bbc\nbc.txt")

print('aa', end=', ')# print 라인스킵 속성이 들어가있다.
print('bb')









