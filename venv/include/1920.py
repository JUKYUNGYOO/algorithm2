# https://www.acmicpc.net/problem/1920
#
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을
# 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …,
# A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수들의 범위는 int 로 한다.
#
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
#
# 1
# 1
# 0
# 0
# 1

n = int(input())
array = set(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))
for i in x:
    if i not in array:
        print('0')
    else:
        print('1')




