# 클래스의 이해

kor = 100   # 전역변수

def abc():  # 함수
    a = 10  # 지역변수
    print('함수')
    
class MyClass:  # 클래스
    kor = 90    # 멤버변수
    
    """
    def __init__(self):
        pass
    """
    
    def abc(self):
        print('메소드')
    
    def show(self):
        # kor = 80    # 지역변수
        print(self.kor)
        print(kor)  # 지역변수를 참조하다가 없으면 전역변수를 참조 한다.
        self.abc()  # 메소드를 콜
        abc()   #함수를 콜

my = MyClass()
my.show()
