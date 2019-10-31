# adj = [[1] for _ in range(5)]
# print(adj)
#
from collections import deque

# 새로운 queue 생성
numbers = deque()

# queue에 값 추가
numbers.append(2)
numbers.append(3)
numbers.append(5)
numbers.append(7)


# queue에서 하나 제거
x = numbers.popleft()
print(numbers)
print(len(numbers))