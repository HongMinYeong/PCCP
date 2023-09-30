# 2번의 반복이 필요하다
#
# 1. 막대기에서 가장 큰 수를 오른쪽으로 옮기는 반복
#
# 2. 막대기의 사이즈를 줄여가는 반복

lst = [3, 5, 1, 13, 8, 4]

for i in range(len(lst) - 1, 0, -1):
    for j in range(0, i):
    # for j in range(0, len(lst)-1):
        #  왼쪽이   오른쪽보다    크면? 작으면?
        if lst[j] > lst[j + 1]:
            # 두개의 자리를 바꾸어 주겠어!
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)






