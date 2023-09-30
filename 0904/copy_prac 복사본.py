
a = 11

a2 = a

a = 123

print(a)
print(a2)
print()

b = "string"

c = [1, 2, 3]

c2 = c[:]

c[0] = 100

print(c)
print(c2)
print()

d = [1, 2, 3]

d2 = d

d = 100

print(d)
print(d2)

mat = [
    [0, 0],
    [0, 0]
]

mat2 = mat[:]

mat[0][0] = 100

print(mat)
print(mat2)


from copy import deepcopy

deepcopy()

# 1. 1차원 리스트는 슬라이싱 활용한 얕은 복사 ( [:])
# 2. 다차원 리스트는 deepcopy 사용
