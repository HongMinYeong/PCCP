# 2번의 반복 필요

# 1. 막대기에서 가장 큰 수를 오른쪽으로 옮기는 반복

# 2. 막대기의 사이즈를 줄여가는 반복 

lst = [3,5,1,13,8,4]

for i in range(len(lst)-1,0,-1): #i는 6부터 시작하므로 1 빼주깅 
    for j in range(i): #각 시행 횟수 안에서 , 5 4 3 2 1 번씩 비교할 거여! (for j in range(0,i):) 써도 됨 
        #왼쪽이 오른쪽보다 크면? 작으면??
        if lst[j]>lst[j+1]:
            #두개의 자리를 바꾸어 주겠다능! 
            lst[j], lst[j+1] = lst[j+1],lst[j] #동시에 진행해야됨 (동시할당)
            #j+1 = i가 될때까지 진행 

print(lst)