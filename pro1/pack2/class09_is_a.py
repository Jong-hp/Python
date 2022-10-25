# 클래스의 상속 : 다형성을 구사 가능

class Animal:
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal):  # 상속
    def __init__(self):
        print('Dog 생성자')    # 자식의 생성자가 있을시 자식 생성자만 호출된다.
        
    def my(self):
        print('난 댕댕이~')


dog1 = Dog()
dog1.move()
dog1.my()

print()
class Horse(Animal):    # 부모(Animal)
    pass

horse1 = Horse()
horse1.move()
