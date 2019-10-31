# https://www.acmicpc.net/problem/10930

# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.
#
# Baekjoon
# 9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857

import hashlib

input_data = input()
encoded_data = input_data.encode()
# 입력받은 데이터의 byte객체를 불러움
result = hashlib.sha256(encoded_data).hexdigest()
print(result)