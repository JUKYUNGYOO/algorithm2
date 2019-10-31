#
# Class Inheritance(상속)
# 기존에 정의해둔 클래스의 기능을 그대로 물려받을 수
# 있다.
# 기존 클래스에 기능 일부를 추가하거나, 변경하여
# 새로운 클래스를 정의한다.
# 코드를 재사용할 수 있게 된다.
# 상속받고자 하는 대상인 기존 클래스는
# (Parent,Super,Base class 라고 부른다.)
# 상속받는 새로운 클래스는(Child,Sub,Derived class)
# 라고 부른다.
# 의미적으로 is-a관계를 갖는다.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self,food):
        print('{}은 {}를 먹습니다.'.format(self.name,food))

    def sleep(self,minute):
        print('{}은 {}분 동안 잡니다.'.format(self.name,minute))
    def work(self,minute):
        print('{}은 {}분 동안 준비합니.'.format(self.name,minute))

# Student,Employee 클래스는 Person의 상속을 받는다.
# class Student(Person):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
class Employee(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def work(self,minute):
        super().work(minute)
        print('{}은 {}분 동안 업무를 합니다'.format(self.name,minute))


# 부모클래스의 기능을 그대로 이용 할 수 있다.
# 상속의 개념



bob = Employee('Bob',25)
bob.eat('bbq')
bob.sleep(30)
bob.work(50)

#
# method override
# 부모클래스의 method를 재정의(override)
# 하위 클래스(자식 클래스)의 인스턴스로 호출시,
# 재정의된 메소드가 호출됨
class Student(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self,minute):
        super().work(minute)
        print('{}은 {}분 동안 공부합니다.'.format(self.name,minute))
# 학생 클래스에서 work를 재정의

bob =  Student('bob',25)
bob.eat('bbq')
bob.sleep(10)
bob.work(10)


# override하게 되면 부모클래스의 기능이
# 쓸모 없어 지는데
# 이때 사용하는 것이 super()메소드 이다.

#
# 부모클래스 의 있는 기능은 그대로 가지고
# 와서 이용가능,
# Override하면 부모클래스의 기능은 배제
# 하지만 super()를 사용하면 부모클래스의
# 메소드 사용 가능

# special method
# __로 시작 __로 끝나는 특수 함수
# 해당 메소드들을 구현하면, 커스텀 객체에 여러가지
# 파이썬 내장 함수나 연산자를 적용가능
# 오버라이딩 가능한 함수 목록은 아래 링크에서 참조
#
# https://docs.python.org/3/reference/datamodel.html





