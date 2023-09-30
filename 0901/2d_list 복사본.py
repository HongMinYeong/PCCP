d = [[0, 1],
[0, -1],
[1, 0],
[-1, 0]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x = 1
y = 1

lst = [
    [0,0,0],
    [0,1,0],
    [0,1,0]
]

for direction in d:
    nx = x + direction[0]
    ny = y + direction[1]
    if lst[nx][ny] == 1:
        # 이동을 하겠어.
        x = nx
        y = ny

for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]