# https://www.acmicpc.net/problem/1991

class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
# 자기 자신에 대해서 데이터 출력후
# 왼쪽과 오른쪽을 방문한다.
def pre_order(node):
    print(node.data,end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])
#왼쪽방문, 루트처리, 오른쪽 방문
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data,end='')

    if node.right_node != '.':
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data,end='')

n = int(input())
tree = {}
# 노드의 정보를 tree라는 dict 자료형에 넣음
for i in range(n):
    data, left_node,right_node = input().split()
    tree[data] = Node(data,left_node,right_node)
# tree에 대해서 데이터를 넣어주고
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])


