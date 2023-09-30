arr = [6, 3, 7, 2, 5, 8, 11, 13]

def merge_sort(lst):

    if len(lst) == 1:
        return lst

    mid = len(lst)//2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)


# def merge(left, right):
#     l = 0
#     r = 0
#     idx = 0
#
#     result = [0] * (len(left) + len(right))
#
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             result[idx] = left[l]
#             l += 1
#             idx += 1
#         else:
#             result[idx] = right[r]
#             r += 1
#             idx += 1
#
#     while  l < len(left):
#         result[idx] = left[l]
#         l += 1
#         idx += 1
#
#     while r < len(right):
#         result[idx] = right[r]
#         r += 1
#         idx += 1
#     return result


def merge(left, right):
    l = 0
    r = 0

    result = []

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])
    return result

print(merge_sort(arr))








