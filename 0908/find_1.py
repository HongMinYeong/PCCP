# 코드 수정해야됨 
import sys
from pprint import pprint
from collections import deque


# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000

n = map(int,input())
lst = [list(map(int,input())) for _ in range(n)]
print(lst)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

stack = deque()
cnt = 0

while stack: #스택이 비어질때 까지 반복 돔 
    x,y = stack[-1] #가장 위에있는 곳 바라봄 
    cnt += 1
    for d in range(4): 
        nx = x + dx[d]
        ny = y + dy[d]
        #방문항 수 있는 후보지를 찾아 
        if ny<0 or ny>=n or nx<0 or nx>=n:
            #그리드를 벗어난 것이ㅑ
            #다음번 for문을 진행을 해야한다.
            continue
        if lst[nx][ny] == 1:
            stack.append((nx,ny))
            lst[nx][ny] = 0
    
        





