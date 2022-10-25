# 정규 표현식 : 다량의 데이터에서 원하는 데이터만 선택해서 처리할 때 효과적

import re

ss = "12_1234 abc가나다abc_nbcABC_123555_6한국Python is fun."
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r'가나다', ss))
print(re.findall(r'1', ss))
print(re.findall(r'[1-2]', ss)) # [0-0] 범위를 줄수있다
print(re.findall(r'[0-9]', ss)) # [0-0] 범위를 줄수있다 
print(re.findall(r'[0-9]+', ss)) # [0-0 범위를 줄수있다, + = (하나이상) 
print(re.findall(r'[0-9]{2}', ss)) # [0-0] 범위를 줄수있다
print(re.findall(r'[0-9]{2,3}', ss)) # [0-0] 범위를 줄수있다, {0,0} = 횟수
print(re.findall(r'[a-z]+', ss)) # 소문자
print(re.findall(r'[A-Za-z]+', ss)) # 대문자
print(re.findall(r'[가-힣]+', ss)) # 한글
print(re.findall(r'[^가-힣]+', ss)) # 한글 # ^ = 부정
print(re.findall(r'12/34', ss))
print(re.findall(r'.bc', ss))
print(re.findall(r'....', ss))
print(re.findall(r'[^1]+', ss))
print(re.findall(r'^1+', ss)) # 시작하는글자
print(re.findall(r'fun.$', ss)) # 끝나는글자

print(re.findall(r'\d', ss))
print(re.findall(r'\d+', ss))
print(re.findall(r'\s', ss))
print(re.findall(r'\S', ss))
print(re.findall(r'\d{1,3}', ss))

print()
p = re.compile('the', re.IGNORECASE) # 대문자 소문자 구분 안하는 플래그
print(p)
print(p.findall('The do the dog'))
print()
ss = '''My name is tom.
I am happy'''
print(ss)
p = re.compile('^.+', re.MULTILINE) # 열이 달라도 합쳐서 표현을 한다.
print(p.findall(ss))











