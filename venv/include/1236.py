# https://www.acmicpc.net/problem/1236

# 문제
# 영식이는 직사각형 모양의 성을 가지고 있다.
# 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다.
# 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.
#
# 성의 크기와 경비원이 어디있는지 주어졌을 때,
#  몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지
# 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다.
# N과 M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다.
# 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.
# 4 4
# ....
# ....
# ....
# ....
#
# 대각선에 경비원을 두고 간다면
# 모든 행과 열에 경비원을 두고 간다.


n,m = map(int,input().split())
array = []

for _ in range(n):
    array.append(input())

row = [0] * n
column = [0] * n

for i in range(n):
    for j in range(n):
        if array[i][j] == 'X': #경비원이 존재하는 위치 X
            row[i] = 1
            column[j] = 1
# 행에 대해서 반복문을 돌면서
# 경비원이 존재하지 않는 행에 count+=1
row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count +=1
# 열에 대해서 반복문을 돌면서
# 경비원이 존재하지 않는 열에 count+=1

column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1;
print(max(row_count,column_count))




























