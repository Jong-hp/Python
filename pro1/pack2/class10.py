# 클래스의 상속
class Person:
    say = '난 사람~'
    nai = '22'
    __kbs = '공영방송' #private 멤버 변수 # __kbs에 __ 는 Person에서만 유효한다.
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나야:{}, 이야기:{}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        
print(Person.say, Person.nai)
# person.printInfo()
p = Person('24')
p.printInfo()
p.hello()

print('**Employee**' * 3)
"""
class Employee(Person):
    pass

emp = Employee('26')
emp.printInfo()
"""
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자')
        
    def printInfo(self):
        print('Employee의 printInfo 메소드')
        
    def empPrintInfo(self):
        print(self.say, self.nai, self.subject)
        print(self.say, super().say, self.nai, super().nai) # super(부모만 본다)
        self.printInfo()                                    # self 생성자 따라 출력된다.
        super().printInfo()
        self.hello()
        # print()(super().say, super().__kbs)  # 'super' object has no attribute '_Employee__kbs'  
        
emp = Employee()
emp.printInfo()
emp.empPrintInfo()

print('**Worker**' * 3)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)   # 부모 생성자 호출

    def wPrintInfo(self):
        self.printInfo()
        
wor = Worker('28')
print(wor.say, wor.nai)
wor.printInfo()


print('--Programmer--' * 3)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai)   # Bound call
        Worker.__init__(self, nai) # Unbound call
        
    def ProShow(self):
        self.printInfo()
        
pr = Programmer('30')
print(pr.say, pr.nai)
pr.ProShow()

print('~~~~~~~~~~~~~~~~~~~~~')
print(type(3))
print(type(pr))
print(type(wor))
print(Programmer.__bases__, Worker.__bases__, Person.__bases__)







