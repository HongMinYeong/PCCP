import sys
from pprint import pprint
from collections import deque

sys.stdin = open('dfs_input.txt')

n, e = map(int,input().split())

lst = [[] for _ in range(n+1)]

for _ in range(e):
    s_node, e_node = map(int,input().split())
    lst[s_node].append(e_node)
    lst[e_node].append(s_node)

pprint(lst)
#
#

start_node = 1

visited = set()

def dfs(node):
    visited.add(node)
    print(node)

    for next_node in lst[node]:
        if next_node not in visited:
            dfs(next_node)


dfs(start_node)

#
# visited = set()
# visited.add(start_node)
# def dfs(node):
#     print(node)
#
#     for next_node in lst[node]:
#         if next_node not in visited:
#             visited.add(node)
#             dfs(next_node)
