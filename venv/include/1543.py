# https://www.acmicpc.net/problem/1543
#
# 세준이는 영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 한다.
# 이 함수는 어떤 단어가 총 몇 번 등장하는지 세려고 한다.
# 그러나, 세준이의 함수는 중복되어 세는 것은 빼고 세야 한다.
# 예를 들어, 문서가 abababa이고, 그리고 찾으려는 ababa라면,
# 세준이의 이 함수는 이 단어를 0번부터 찾을 수 있고, 2번부터도 찾을 수 있다.
# 그러나 동시에 셀 수는 없다.
# 세준이는 문서와 검색하려는 단어가 주어졌을 때,
# 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램을 작성하시오.

# ababababa
# aba
#
# 문서와 단어의 위치를 맞추어서 반복적으로
# 비교합니다.

# 첫째 줄에 문서가 주어진다.
# 문서의 길이는 최대 2500이다.
# 둘째 줄에 검색하고 싶은 단어가 주어진다.
# 이 길이는 최대 50이다.

# O(NM) = 2500 * 50
document = input()
word = input()
index = 0
result = 0

# 단어의 수만큼이동해서 문서를 벗어나지 않을 때까지
while(len(document) - index >= len(word)):
    if document[index:index+len(word)] == word:
        #문서에서 보고 있는 단어가 찾고자 하는 단어인 경우
        # index부터 단어의 길이만큼 확인을 해
        result +=1
        index += len(word)
    else:
        index += 1
         # 단어를 찾지 못한 경우에는 한칸이동
print(result)