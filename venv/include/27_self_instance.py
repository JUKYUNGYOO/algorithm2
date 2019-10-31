class Person:
    def __init__(self,name,age):
        print('self:',self)
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name,'go to sleep')

a = Person('Aaron',20)
b = Person('Bob',30)


print(a)
print(b)

a.sleep()
b.sleep()

