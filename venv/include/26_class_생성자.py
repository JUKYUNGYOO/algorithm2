#
# __init__(self)
#
# 생성자, 클래스 인스턴스가 생성될 때 호출됨
# self인자는 항상 첫번째에 오며 자기 자신을 가리킴
# 이름이 꼭 self일 필요는 없지만, 관례적으로
# self로 사용
# 생성자에서는 해당 클래스가 다루는 데이터를 정의
# 이 데이터를 멤버변수 또는 속성이라고 함.
#
# self
# 파이썬의 method는 항상 첫번째 인자로
# self를 전달
# self는 현재 메쏘드가 호출되는
# 객체 자신을 가리킴

class Person:
    def __init__(self,name,age=10):
        print(self, 'is generated')
        self.name = name
        self.age = age
#  self.속성의 이름 = 파라미터
p1 = Person('Bob',30)
p2 = Person('Kate',20)
p3 = Person('Aaron')


print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)


