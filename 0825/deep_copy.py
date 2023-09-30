lst1 = [1, 2, 3]

lst2 = [1, 2, 3]

lst3 = lst1

# print(lst1)
# print(lst2)
# print(lst3)

lst1[0] = 100

print(lst1)
print(lst3)

print()
lst4 = lst1[:]

lst1[1] = 10000

print(lst1)
print(lst4)

lst1 = 3
print(lst3)


matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


copied_matrix = matrix[:]

from pprint import pprint


matrix.append(123)
pprint(copied_matrix)


# matrix[0][0] = 100
# pprint(copied_matrix)
#
#
# matrix[0] = 300
#
# pprint(copied_matrix)

from copy import deepcopy






# 1. 리스트를 반복할때는 얕은 복사 ([:]) 을 사용한다
# 1.a 단, 2차원 리스트의 경우에는 깊은 복사(from copy import deepcopy)를 사용한다





