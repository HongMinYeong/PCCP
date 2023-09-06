
################################################

# m=size[0]
# n=size[1]

#m줄이니까 "입력"이라는 행위를 m 번 반복해야함
open('input.txt') #파일 오픈
#'입력'이라는 것으로 넣어줌
import sys
sys.stdin = open('input.txt')

m, n = list(map(int,input().split())) #가로 세로 입력받기

# matrix = []
# for _ in range(m):
#     lst = list(map(int,input().split()))
#     matrix.append(lst)

# 같은 코드
print(m)
print(n)
matrix = [list(map(int,input().split())) for _ in range(m)]
print(matrix)