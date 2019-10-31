# https://www.acmicpc.net/problem/2250
#

class Node:
    def __init__(self,number,left_node,right_node):
        # parent가 없는 노드가 루트노드이다.
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node,level):
    global level_depth, x
    level_depth = max(level_depth,level)
    # 왼쪽노드 방문
    if node.left_node != -1:
        in_order(tree[node.left_node],level+1)
    # 데이터 처리
    # 해당 레벨에서 가장 작은 값,가장 왼쪽
    level_min[level] = min(level_min[level],x)
    # 해당 레벨에서 가장 큰 값 ,가장 오른쪽
    level_max[level] = max(level_max[level],x)
    x+=1
    # 오른쪽 노드 방문
    if node.right_node != -1:
        in_order(tree[node.right_node],level+1)

n = int(input())
tree = {}
# min은 가장 너비가 클 수 있는 n
level_min = [n]
# max는 가장 너비가 작은 0
level_max = [0]
root = -1
x = 1
level_depth = 1
# 노드의 개수에 대해서 트리를 초기화
for i in range(1,n+1):
    tree[i] = Node(i,-1,-1) #좌,우 비어있음,초기화
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    number,left_node,right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number
# 부모가 없는 노드를 루트라고 가정하고
for i in range(1,n+1):
    if tree[i].parent == -1:
        root = i
in_order(tree[root],1)
# 그 루트에서 부터 중위순회


result_level = 1
result_width = level_max[1] - level_min[1]+1
for i in range(2,level_depth+1):
    width = level_max[i] - level_min[i] + 1
    #  너비가 가장 넓을 때
    if result_width < width:
        result_level = i
        resilt_width = width
print(result_level,result_width)











