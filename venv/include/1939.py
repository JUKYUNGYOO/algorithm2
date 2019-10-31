# https://www.acmicpc.net/problem/1939

from collections import deque

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]


# bfs 경로 있는지
def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int,input().split())
    # 연결되어 있는 간선의 정보
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    # start,end 초기화
    start = min(start, weight)
    end = max(end, weight)

start_node,end_node = map(int,input().split())

result = start
# 중량에 대해 이진탐색
while(start <= end):
    mid = (start+end) // 2
    # mid는 현재의 중량을 의미합니다.

    # 이동가능, 중량을 증가시킵니다.
    if bfs(mid):
        result = mid
        start = mid+1
    # 이동 불가능, 중량 감소
    else:
        end = mid - 1

print(result)
# 이동가능한 중량  = result













