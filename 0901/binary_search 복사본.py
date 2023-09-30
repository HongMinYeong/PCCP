lst = list(range(1, 9))

def binary_search(s, e, target):
    if e < s:
        return False
    mid = (s + e)//2
    if lst[mid] == target:
        print('찾았다!')
        return True

    if lst[mid] > target:
        return binary_search(s, mid - 1, target)
    elif lst[mid] < target:
        return binary_search(mid+1, e, target)