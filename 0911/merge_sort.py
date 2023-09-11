#병합정렬
#코드 다시 
arr = [6,3,7,2,5,8,11,13]

# 분할정복 
def merge_sort(lst):
    
    # 끝나는 조건
    if len(lst) ==1:
        return lst
    
    #나누는 과정 
    mid = len(lst)//2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted,right_sorted)

#합치는 과정 
def merge(left,right):
    l = 0 # left
    r = 0 # right
    idx = 0

    result = [0]*(len(left) + len(right))

    # while l<len(left) and r <len(right):
    #     if left[l] <= right[r]: # 작은애를 넣자 
    #         result[idx] = left[l]
    #         l += 1 #그리고 한칸씩 이동
    #         idx += 1 #그리고 한칸씩 이동 
        
    #     else:
    #         result[idx] = right[r]
    #         r += 1
    #         idx += 1


    result.extend(left[l:]) #남은거 각각 붙여 extend 남은녀석들을 각각 append 
    result.extend(right[r:])

    return result

#확인
print(merge_sort(arr))

