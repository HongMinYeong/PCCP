import sys
from collections import deque


sys.stdin = open('dfs_input.txt')

node_num, edge_num = map(int,input().split())
dfs_input = [list(map(int,input().split())) for _ in range(edge_num)]
#인접 리스트

adjacency_list = [[] for _ in range(node_num + 1)]
for _ in range(edge_num):
    s, e = map(int, input().split())
    adjacency_list[s].append(e)
    adjacency_list[e].append(s)

# visited = set()
visited = list()

stack = deque()
start_node = 1

stack.append(start_node)

while stack: #stack에 들어있을때까지 반복을하겠다!
    print(stack)
    node = stack.pop()
    
    if node not in visited:
        visited.append(node)

    for next_node in adjacency_list[node]:
        if next_node not in visited:
            stack.append(next_node)


print(*visited) #[1,2,3,4,5,6] ->1,2,3,4,5,6 unpacking 해주는 거임 (*)

# for i in visited:
#     print(i , end = " ")
# print()
# 위에 print랑 똑같은거임 

visited = set() 

stack = deque()

start_node = 1

stack.append(start_node)
visited.add(start_node)



while stack:
    node = stack[-1]

    for next_node in adjacency_list[node]:
        if next_node not in visited:
            stack.append(next_node)
            visited.add(next_node)
            print(next_node)


            break #1번에서 3번을 stack에 넣지 않기 위해 
        else:
            stack.pop() #다 방문했다면 나가! 

print(visited)

print(*visited)

