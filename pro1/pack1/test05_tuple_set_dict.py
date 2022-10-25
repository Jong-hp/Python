# 묶음형 자료형 
from dask.array import lib
print('---- tuple ----')
# tuple - list와 유사하나 읽기 전용(list 보다 속도 빠름 ). 순서O, 수정X
t = ('a', 'b', 'c', 'a') # 가독성을 위해 () 권장
t = 'a', 'b', 'c', 'a' # 가능함
print(t, type(t), len(t), t.count('a'), t.index('b'))

print(t[0])
# t[0] = 'k' # 'tuple' object does not support item assignment - tuple운 수정 불가

imsi = list(t)
print(imsi, type(imsi))
imsi[0] = 'k'
t = tuple(imsi) # tuple 은 검색에 용이 하나, 수정은 list에서 수정한다.
print(t)

print()
print((1), type((1)))
print((1,), type((1,)))

print()
t1 = (10, 20)
a, b = t1
b, a = a, b # 자리 바꿈
t2 = a, b
print(t2)

print('---- set ----')
# 순서X, 중복X
a = {1,2,3,1}
print(a, type(a), len(a)) # 중복이 허용이 안됨

b = {3, 4}

print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a - b) # 차집합
print(a | b) # 합집합
print(a & b) # 교집합

print()
print(a)
# print(a[0])  # TypeError: 'set' object does not support item assignment 순서가 없다.
# a[0] = 100 # err

a.update({4,5}) # 함수를 이용한 추가 가능
a.update([6,7,8])
a.update((9,))
print(a)

a.discard(3)  # 값에 의한 삭제
a.remove(5)   # 값에 의한 삭제
a.discard(3)  # 해당값이 없으면 스킵
# a.remove(5)   # 해당값이 없으면 err
print(a)

c = set() # 얕은 복사
c = a
print(c)
a.clear()
print(a)
print(c)

print()
li = [1,2,3,1,2,3]
print(li)
imsi = set(li) # 중복 제거
li = list(imsi)
print(li)

print('---- dict ----')
# 사전형 : {'key' 'value'} - 순서X, key를 이용해 value를 참조
my = dict(k1=1, k2='mbc', k3=3.4)
print(my, type(my))

dic = {'파이썬':'뱀','자바':'커피','스프링':'용수철', '점수':[60, 70, 90]}
print(dic, type(dic), len(dic))
print(dic['자바']) # value 값을 얻을 수 있다.
# print(dic[0]) # err

dic['오라클'] = '예언자' # 추가 가능
print(dic)
del dic['오라클'] # 삭제
dic.pop('파이썬') # 삭제
print(dic)
dic['자바'] = '웹용언어' # 수정 가능
print(dic)

print(dic.keys()) # keys값만 얻음
print(dic.values()) # values값만 얻음
print('파이썬' in dic) # bool


# str : 순서O, 수정X
# list : 순서O, 수정O [ ]
# tuple : 순서O, 수정X ( )
# set : 순서X, 수정X, 중복X { }
# dict : 순서X, 키에 의해 value 참조 {'키','값'}





