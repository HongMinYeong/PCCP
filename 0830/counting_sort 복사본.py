n = 3
lst = [0, 1, 3, 3, 2, 2, 1, 0, 1]

counting_lst = [0] * (n + 1)

for i in lst:
    counting_lst[i] += 1

print(counting_lst)
old_counting_lst = counting_lst[:]

for i in range(1, len(counting_lst)):
    counting_lst[i] = counting_lst[i] + counting_lst[i-1]

print(counting_lst)

lst = [0, 1, 3, 3, 2, 2, 1, 0, 1]
# 꺼꾸로 반복을 돌 예정입니다.
# 1. 리스트를 뒤집어서 반복을 돌 수 있죠

sorted_lst = [0]*len(lst)
for num in lst[::-1]:
# for index in range(len(lst)-1, -1, -1):
#     num = lst[index]
    put_index = counting_lst[num] - 1
    sorted_lst[put_index] = num

    counting_lst[num] = counting_lst[num] - 1

print(sorted_lst)


# sorted_lst = []
# for index in range(len(old_counting_lst)):
#     value = old_counting_lst[index]
#     sorted_lst += [index] * value
#
#
# print(sorted_lst)
#
#


lst.sort()





