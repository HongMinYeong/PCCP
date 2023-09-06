n = 5
# 1. 오른쪽으로 진행
# 2. 아래로 진행
# 3. 왼쪽으로 진행
# 4. 위로 진행 
#세로
dx = [0,1,0,-1] #nx[0]//nx[1]...
#가로
dy = [1,0,-1,0] #ny[0]//ny[1]...

snail = [[0]*n for _ in range(n)] # 5X 5 빈 격자

x, y = 0,0
d = 0  #direction 
for num in range(1,n**2 + 1):
    print(x,y,num)
    snail[x][y] = num
# x,y라는 애들을 이동시켜줘야돼
    nx = x + dx[d]
    ny = y + dy[d]
    # if nx,ny가 그리드를 벗어난 순간에는 방향을 바꿔줘야 겠다. 
    # 하나라도 해당되면 방향이 바뀌어야 함 
    if ny < 0 or ny >= n or nx < 0 or nx >= n or snail[nx][ny]:
        d = (d + 1)%4
        nx = x + dx[d]
        ny = y + dy[d]
    
    x,y = nx,ny

    for i in snail: # 격자 프린트 
        print(i)

    print()

