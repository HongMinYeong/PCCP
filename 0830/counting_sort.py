# 카운팅 정렬 코드
n=3 #끝이 3칸짜리 
lst = [0, 1, 3, 3, 2, 2, 1, 0, 1]

# counting_lst = [0] * (max(lst) + 1)  # 갯수 세는 리스트 [max(lst)->3]

counting_lst = [0] * (n+1)
for i in lst:  # 일단 몇개씩 있는지 카운트
    counting_lst[i] += 1

print(counting_lst)    #[2,3,2,2]
#0이 2개, 1이 3개,2가 3개,3이 2개
# ------------------------------------------------------------------------------
old_counting_lst = counting_lst[:]

for i in range(1,len(counting_lst)):
    counting_lst[i] = counting_lst[i]+counting_lst[i-1]

print(counting_lst) #[2,5,7,9]
# ------------------------------------------------------------------------------
lst = [0, 1, 3, 3, 2, 2, 1, 0, 1]
#거꾸로 반복을 돌 예정.
# 1. 리스트를 뒤집어서 반복을 돌 수 있음
#stable하게 하깅 
sorted_lst = [0]*len(lst)
for num in lst[::-1]:
# 아래랑 똑같음
# for index in range(len(lst)-1,-1,-1):
    # num = lst[index]
    put_index = counting_lst[num] -1 #가리키는것에 왼쪽 
    sorted_lst[put_index] = num
    counting_lst[num] = counting_lst[num] - 1

print(sorted_lst)
# ------------------------------------------------------------------------------


# sorted_lst = []
# for index in range(len(old_counting_lst)):  
#     value = old_counting_lst[index]
#     print(value)
#     sorted_lst += [index] * value

# print(sorted_lst)