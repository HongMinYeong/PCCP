[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# lst= [0,0,0,0]
lst = [0] * 5

matrix = []

for i in range(5):
    matrix.append(lst)

matrix[0][0] =1 #1이 전체가 채워짐
#다 lst여서 복사됨
print(matrix)

