lst1 = [1,2,3]

lst2 = [1,2,3]

lst3 = lst1

# print(lst1)
# print(lst2)
# print(lst3)

lst1[0] = 100
print(lst1)
print(lst3)

#lst1의 주소가 lst3에 할당되어있기 떄문에 lst1의 값이 바뀌면 lst3도 바뀜

lst4 = lst1[:] #lst1의 값을 처음부터 끝까지 값만 복사

lst1[1] = 10000
print(lst1)
print(lst4)

lst1 = 3
print('lst1은 ',lst1)
print('lst3은 ',lst3)

matrix = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

copied_matrix = matrix[:]

from pprint import pprint
pprint(copied_matrix)
# matrix[0][0] = 100
# pprint(copied_matrix) #왜 값만 복사가 안될까?
# #리스트로 이루어진 리스트 (deep_copy 모듈사용.,.,.,.,.,)
# matrix[0] = 300
# pprint(matrix)
# pprint(copied_matrix) #아까는 matrix가 list로 이루어진 녀석이었는데 그래서 어디선가 가져오고 가져오고 가져왔는데

matrix.append(123)
pprint(copied_matrix) #안바뀜 새롭게 생긴 주소는 복사 안됨 copied_matrix = matrix였으면 복사됨


