# https://www.acmicpc.net/problem/4195

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    # x와 y가 서로 다르다면
    # y의 부모를 x로 설정한다.

    if x!=y:
        parent[y] = x
        number[x] += number[y]
# x 네트워크의 크기 값에 y 네트워크의 크기를 더해주면
test_case = int(input())
for _ in range(test_case):
    parent = dict()
    number = dict()
    # dict() key-value쌍을 갖는 tuple리스트를 받아들 임 .

    f = int(input())

    for _ in range(f):
        x,y = input().split(' ')
        # parent를 가지고 있지 않다면 network의 크기를 1로 설정
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x,y)
    #     2개를 네트워크에 포함시킴, x,y를 이어줌
    print(number[find(x)])
#
#
# 1) Fred Barney
# 2) Betty Wilma
# 3) Barney Betty
#
# Fred -> Fred
# Barney -> Fred
# Betty -> Fred
# Wilma -> Fred
#
#
# Fred   Betty
#   |   /  |
#   |  /   |
# Barney Wilma
#
# Fred   4
# Barney 4
# Betty  4
# Wilma  4
#
#
#
#
#




