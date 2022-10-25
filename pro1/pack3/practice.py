# 1번
from cryptography.x509 import name
li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2] # 리스트 타입
im = set(li)
li = list(im)
print(li)

# 2번
for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end = ' ')
    
# 6번
a = 1; b = 2; c = 3;
def Foo():
    a = 20
    b = 30
    def Bar():
        global c
        nonlocal b
        print('Bar 내의 a:{}, b:{}, c:{}'.format(a, b, c))
        c = 40
        b = 50
    Bar()
Foo()

# 7번
*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1)
print(v2)
print(v3)

# 8번
Hap=lambda m,n:m+n*5
print(Hap(1,2))

# 9번
print(list(range(1, 6, 2)))

# 10번 : 아래 코드에서 키보드를 통해 0이 입력되면 에러가 발생하게 된다.
# 예외처리를 위한 코드 try ~ except를 이용하여 0 이외의 정수 값은 정상 실행되고 0은 에러 메세지를 출력하도록 변경된 코드를 적으시오.

# try:
#     aa = int(input())
#     bb = 10 / aa
#     print(bb)  # 결과값을 출력하는것까지 포함인지 몰라서 추가했습니다.
# except ZeroDivisionError:
#     print('0으로 나누면 안되요')
#

    
# 11번: 별찍기
i = 10
while i > 0:
    print(' '*(10-i)+'*'*i)
    i -= 1
    
# # 12번:  tom과 james는 커피를 마시며 윤년에 대한 대화를 나누고 있었다.
# tom에 의하면 윤년은 과년이라고도 하며, 역법인 태음력이나 태양력에서, 자연의 흐름에 대해서 생길 수 있는 오차를 보정하기 위해 삽입하는 날이나 주, 달이 들어가는 해를 말하는데, 윤년인 해에는 2월달이 29일이 된다고 한다.
# 이런 얘기를 듣던 james가 노트북을 켜더니 파이썬의 if문을 이용하여 프로그램을 작성했다.
# james가 키보드를 이용하여, 연도를 입력해 실행한 결과는 아래와 같다. james가 작성한 코드를 적어 보시오.
# 처리 조건 : 연도는 4의 배수이고 100의 배수가 아니거나 400의 배수이면 윤년이다.
#
# 실행 2회 실행 예)
# 연도 입력:2020
# 2020년은 윤년
# 연도 입력:2022
# 2022년은 평년 (배점:10)

# year=int(input('연도 입력:'))
# if year%4==0:
#     if year%100!=0 or year%400==0:
#         print('{}년은 윤년'.format(year))
#     else:
#         print('{}년은 평년'.format(year))            
# else:
#     print('{}년은 평년'.format(year))


# 13번 :  while 문을 사용 : 1 ~ 100 사이의 정수 중에서 3으로 끝나는 숫자만 출력하는 코드를 작성 하시오.
# 출력 결과는 아래와 같다.
# 3 13 23 33 43 53 63 73 83 93
#
# 아래 소스 코드의 빈 칸을 차례대로 채우시오. (배점:10)
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue         
               
    if i > 100: break 
                 
    print(i, end=' ')
    i += 1
    
# 14번 : 원격 데이터베이스 서버의 테이블과 연동하는 프로그램을 작성하려고 한다.
# 아래의 출력 예와 같이 키보드로 직급을 입력받아 해당 직급의 직원을 출력하는 코드를 작성하시오.
# 출력 대상은 직원번호, 직원명, 직급, 부서번호 이다.
#
# 조건 : 테이블은 MariaDB의 jikwon을 사용하기로 한다.
#
# 출력 예)
# 직급 입력: 과장
# 3 이순신 과장 20
# 8 김기만 과장 20
# 12 박별나 과장 40
# 18 이순기 과장 30
# 23 김기만 과장 30
# 27 박하나 과장 20 (배점:10)
print()
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:            
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    jik_info = input('직급 입력: ')
    sql = """
        SELECT jikwon_no, jikwon_name, jikwon_jik, buser_num
        FROM jikwon INNER JOIN buser on jikwon.buser_num=buser.buser_no
        WHERE jikwon_jik='{0}'
    """.format(jik_info)
    
    cursor.execute(sql)
    datas = cursor.fetchall()

    for jikwon_no, jikwon_name, jikwon_jik, buser_num in datas:
        print(jikwon_no, jikwon_name, jikwon_jik, buser_num)

except Exception as e:
    print('err : ', e)
finally:
    cursor.close()
    conn.close()
    
# 15번
#
# 출력 결과)
# gildong = Bicycle('길동', 2, 50000) # name, wheel, price
# gildong.display()
#
# 길동님 자전거 바퀴 가격 총액은 100000원 입니다 (배점:10)

class Bicycle:
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price
        
    def display(self):
        print('{}님 자전거 바퀴 가격 총액은 {}원 입니다'.format(self.name, self.wheel * self.price))
        
gildong = Bicycle('길동', 2, 50000)
gildong.display()