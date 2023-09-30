[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

from pprint import pprint


# lst = [0, 0, 0, 0]
# lst = [0] * 5
#
# matrix = []
# for _ in range(5):
#     matrix.append(lst)
#
#
# pprint(matrix)
#
# matrix[0][0] = 1
#
#
# pprint(matrix)

matrix = []
for _ in range(5):
    matrix.append([0] * 5)

pprint(matrix)

matrix[0][0] = 1

pprint(matrix)
