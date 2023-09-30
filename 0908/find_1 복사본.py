# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000


from collections import  deque

n = int(input())
lst = [list(map(int,input())) for _ in range(n)]
print(lst)



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if lst[i][j]:

            stack = deque()
            # stack = deque([[i,j]])
            stack.append((i,j))
            cnt = 0
            while stack:
                x, y = stack.pop()

                if lst[x][y]:
                    lst[x][y] = 0
                    cnt += 1

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 방문할 수 있는 후보지를 찾아
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        # 그리드를 벗어난 것이야.
                        # 다음번 for문을 진행을 해야 한다.
                        continue

                    if lst[nx][ny] == 1:
                        stack.append((nx, ny))
            print(cnt)








