lst = [3, 5, 1, 13, 8, 4]

for i in range(len(lst)-1): #0부터 4까지 
    #가장 작은 인덱스를 가장 앞으로 넣는 반복 
    min_num_index = i  # 일단 가장 작다고 초기화해두고,
    print('정렬 전 ',lst)
    for j in range(i+1, len(lst)): # 나 다음부터 보면서 ( 나 다음부터 끝까지 )
        # print('-----------다음 ',j,'번째부터----------------')
        if lst[j] < lst[min_num_index]:  # 나보다 작은애가 있으면
            min_num_index = j  # 그 idx를 갱신!
            print('제일 작은수는!',lst[min_num_index])

    lst[i], lst[min_num_index] = lst[min_num_index], lst[i]  
    print('정렬 후',lst)
    # 최종적으로 한번 스왑 min_num_index를 가진 값을 0번째 넣고, 1번째 넣고, 2번째 넣고,,,

print(lst)