
# size = list(map(int,input().split()))
# m = size[0]
# n = size[1]

import sys

sys.stdin = open('input1.txt')

m, n = list(map(int,input().split()))

# m줄이니까 "입력"이라는 행위를 m번 반복을 해야 한다

# matrix = []
# for _ in range(m):
#     lst = list(map(int,input().split()))
#     matrix.append(lst)

matrix = [list(map(int,input().split())) for _ in range(m)]

print(matrix)