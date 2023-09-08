import sys
from pprint import pprint
from collections import deque

sys.stdin = open('dfs_input.txt')

n,e = map(int,input().split())

#인접 행렬의 경우 
# grid = [[0] * (n+1) for _ in range(n+1)]
#
# for _ in range(e):
#     s_node, e_node = map(int,input().split())
#
#     grid[s_node][e_node] = 1
#     grid[e_node][s_node] = 1
#
# pprint(grid)

#인접 리스트 

lst = [[] for _ in range(n+1)]

for _ in range(e):
    s_node, e_node = map(int,input().split())
    lst[s_node].append(e_node)
    lst[e_node].append(s_node)

pprint(lst)


start_node = 1

stack = deque()

stack.append(start_node)

#stack에 append 한순간 방문한 것으로 처리 
visited = set()
visited.add(start_node)

while stack: #스택이 비어질때 까지 반복 돔 
    node = stack[-1] #가장 위에있는 곳 바라봄 
    
    for next_node in lst[node]: #node가 2 면 lst[node] -> [1,4,5]
        if next_node not in visited:
            stack.append(next_node)
            visited.add(next_node)
            break #한번에 한칸만 진행 
    else:
        stack.pop()



