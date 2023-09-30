lst = [9, 3, 7, 2, 5, 8, 11, 13]

def lomuto_partitoin(low, high):
    pivot = lst[high]
    left = low
    for right in range(low, high):
        if lst[right] < pivot:
            lst[left], lst[right] =lst[right], lst[left]
            left += 1

    lst[left], lst[high] = lst[high], lst[left]
    # print(lst, pivot)
    return left

def lomuto(low, high):
    if low < high:
        pivot = lomuto_partitoin(low, high)
        lomuto(low, pivot-1)
        lomuto(pivot+1, high)


lomuto(0, len(lst)-1)
print(lst)



lst = [9, 3, 7, 2, 5, 8, 11, 13]
def hoare_partition(low, high):
    pivot = (low + high) // 2
    l = low
    r = high
    while l < r:
        while lst[l] < lst[pivot] and l < r:
            l += 1
        while lst[r] > lst[pivot] and l < r:
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            lst[l], lst[r] = lst[r], lst[l]
    lst[pivot], lst[r] = lst[r], lst[pivot]
    return r

def hoare(low, high):
    if low < high:
        pivot = hoare_partition(low, high)
        hoare(low, pivot-1)
        hoare(pivot+1, high)
hoare(0, len(lst)-1)
print(lst)



# pivot = lst[-1]
# left = [x for x in lst if x < pivot]
# right = [x for x in lst if x > pivot]
# lst = left + [pivot] + right
#







