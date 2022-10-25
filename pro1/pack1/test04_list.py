# 묶음형(집합형) 자료형 : list - 순서O, 수정O

a = [1, 2, 3]; b = [10, a, 12.5, True, '문자열']
print(a, type(a), id(a))
print(b, type(b), id(b))
aa = []
bb = list()
print(type(aa), type(bb))

print()
family = ['엄마', '아빠', '나', '여동생']
print(family[2]) # 인덱싱
print(family[0:2]) # 슬라이싱
family.append('남동생') # append - 추가
family.insert(0, '할아버지') # insert - 삽입
family.extend(['삼촌', '조카']) # extend - 복수 추가
family += ['이모', '고모'] # += - 추가
family.remove('남동생') # remove - 지우기 ( 값의 대한 삭제)
del family[2] # [ ] - 인덱싱 적용 del - 지우기 ( 순서의 대한 삭제)
print(family, len(family))
print(family.index('나')) # 인덱싱
print('엄마' in family, '할머니' in family) # bool

del family # 변수를 삭제
# print(family)

print() # 수정가능
aa = [1, 2, 3,['a', 'kbs', 'c'], 4, 5] # 중첩 리스트
print(aa)
print(aa[0])
print(aa[3])
print(aa[3][1]) # aa 안에 3번째 안에 1번쨰

print(id(aa))
aa[0] = 333 # 요소값 수정 가능
print(aa, id(aa))


print()
aa2 = ['123', '34', '234']
print(aa2)
aa2.sort()
print(aa2)
aa2.sort(key=int, reverse=True) # 크기 순서
print(aa2)

print()
name = ['소현', '현성', '다정']
print(name)
name2 = name # 얕은 복사 : 주소 치환
print(id(name), id(name2))

import copy
name3 = copy.deepcopy(name) # 깊은 복사, 새로운 객체로 생성

print(id(name), id(name2), id(name3))
name[0] = '용환'
print(name)
print(name2)
print(name3)

# 참고 -------------
print("stack : LiFO, queue : FiFO")
sbs = [1, 2, 3]
sbs.append(4) # 추가
print(sbs)
sbs.pop() # LiFO 뒷자리에서 하나씩 빠진다.
print(sbs)
sbs.pop()
print(sbs)
print()
sbs = [1, 2, 3]
sbs.append(4) # 추가
print(sbs)
sbs.pop(0) # FiFO 앞자리에서 하나씩 빠진다.
print(sbs)
sbs.pop(0)
print(sbs)
