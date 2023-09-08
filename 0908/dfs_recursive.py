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

# pprint(lst)


start_node = 1

visited = set()


def dfs(node):
    visited.add(node)
    print(node)

    for next_node in lst[node]: 
        if next_node not in visited:
            dfs(next_node)
            

#실행 
dfs(start_node)