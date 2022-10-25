# 집합 자료형 : str, list, tuple, set, dict

# 문자열 : str - 순서O : 인덱싱(하나만 참조), 슬라이싱(여러개 참조), 수정X
s = 'sequence'
print(s, type(s), len(s))
print(s.count('e')) # 몇개가 들어가있는지
print(s.find('e'), ' ', s.find('e', 3), s.rfind('e')) # 순서가 몇번째인지
# ...

# 수정 불가
ss = 'mbc' 
print(ss, id(ss))
ss = 'abc' # 참조 대상이 바뀜
print(ss, id(ss))

# 인덱싱, 슬라이싱 대상[start:stop:step]
print(s[0], s[3],) # s[8] err
print(s[-1], s[-3]) # 역순
print(s[0:3], s[3:], s[:3], s[:], s[1:5:2], s[::2])
print(s[-4:-1], s[-3])
print('fre' + s[2:])

print()
s2 = 'kbs mbc'
s2 = ' ' + s2[:4] + 'sbs '+ s2[4:] + ' '
print(s2, len(s2))
print(s2.strip()) # 의미가 없는 공백을 자름 lstrip(),rstrip()
s3 = s2.split(sep=' ')
print(s3)
print(' '.join(s3))

a = 'Life is too long'
b = a.replace('Life', 'Your Leg')
print(b)

