
class Counter:
    def __init__(self):
        self.num = 0

    def increment(self):
        self.num += 1
    def reset(self):
        self.num = 0


    def print_current_value(self):
        print('현재값은:',self.num)
# 클래스 레벨 Counter
# 객체 레벨 c1,c2

c1 = Counter()
c1.print_current_value()
c1.increment()
c1.increment()
c1.increment()
c1.print_current_value()

c1.reset()
c1.print_current_value()


# c2 = Counter()
# c2.print_current_value()

class Math:
    # 전달되는 데이터 보다, 리턴 값이 중요한 경우
    # 내부적인 속성을 유지할 필요가 없는 경
    @staticmethod
    def add(self,a,b):
        return a+b

    @staticmethod
    def multiply(self,a,b):
        return a*b
m = Math()
m.add(1,2)
m.multiply(10,20)

print(m.add(1,2))












