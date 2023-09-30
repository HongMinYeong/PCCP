lst = [3, 5, 1, 13, 8, 4, 2, 30, 18, 23]
print(lst)
# 구간을 줄이는 반복
for i in range(0, len(lst)-1):
    print(i)
    # 가장 작은 인덱스를 가장 앞으로 넣는 반복
    min_num_index = i

    for j in range(i+1, len(lst)):
        if lst[min_num_index] > lst[j]:
            min_num_index = j
            print(min_num_index)
    lst[min_num_index], lst[i] = lst[i], lst[min_num_index]
    print(lst)
    print()

print(lst)