import sys
from pprint import pprint
from collections import deque

sys.stdin = open('dfs_input.txt')

n, e = map(int,input().split())

# 인접 리스트

lst = [[] for _ in range(n+1)]

for _ in range(e):
    s_node, e_node = map(int,input().split())
    lst[s_node].append(e_node)
    lst[e_node].append(s_node)

pprint(lst)
#
#

start_node = 1

queue = deque()
visited = set()

queue.append(start_node)

while queue:
    node = queue.popleft()
    visited.add(node)

    for next_node in lst[node]:
        if next_node not in visited:
            queue.append(next_node)




visited = set()

queue.append(start_node)
visited.add(start_node)

while queue:
    node = queue.popleft()

    for next_node in lst[node]:
        if next_node not in visited:
            queue.append(next_node)
            visited.add(next_node)





