# https://www.acmicpc.net/problem/1302
#
# 김형택은 탑문고의 직원이다.
# 김형택은 계산대에서 계산을 하는 직원이다.
# 김형택은 그날 근무가 끝난 후에,
# 오늘 판매한 책의 제목을 보면서 가장 많이
# 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
#
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때,
# 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다.
# 이 값은 1,000보다 작거나 같은 자연수이다.
# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다.
# 책의 제목의 길이는 50보다 작거나 같고,
# 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다.
# 만약 가장 많이 팔린 책이 여러 개일 경우에는
# 사전 순으로 가장 앞서는 제목을 출력한다.
#
# 예제 입력 1
# 5
# top
# top
# top
# top
# kimtop
# 예제 출력 1
# top


# 횟수 Dictionary
n = int(input())
books = {}   # 책의 등장횟수 , 딕셔너리 자료형

# 데이터를 입력 받을 때 마다
for _ in  range(n):
    book = input()
    # 해당 책이 북스에 들어있지 않는 다면 1로 설정
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
#         등장횟수 += 1
target = max(books.values())  # max(4,1)
# 가장 큰 등장횟수를 넣음
# top 4, kimtop 1
array = []

# top : 4 , kimtop : 1
# book : number
for book, number in books.items():
    if number == target:
        # 등장횟수가 가장 많이 등장한 횟수와 동일 하다면

        array.append(book)
#        array에 담도록 한다.
print(sorted(array)[0])














