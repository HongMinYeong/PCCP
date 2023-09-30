import sys
from pprint import pprint
sys.stdin = open('dfs_input.txt')

node_num, edge_num = map(int,input().split())

dfs_input = [list(map(int,input().split())) for _ in range(edge_num)]

pprint(dfs_input)

# 인접 행렬
adjacency_matrix = [[0] * (node_num + 1) for _ in range(node_num + 1)]

pprint(adjacency_matrix)

for s, e in dfs_input:
    adjacency_matrix[s][e] = 1
    adjacency_matrix[e][s] = 1

print()
pprint(adjacency_matrix)


# 인접 리스트
adjacency_list = [[] for _ in range(node_num + 1)]

for s, e in dfs_input:
    adjacency_list[s].append(e)
    adjacency_list[e].append(s)

for i in adjacency_list:
    print(i)

n = 3
#  3번 노드에서 방문할 수 있는 노드는?

for i in range(node_num + 1):
    if adjacency_matrix[n][i]:
        print(i)
        # i번째 노드에 방문 가능

for i in adjacency_list[n]:
    print(i)






