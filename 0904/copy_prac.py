a = 11 # 숫자

b = "string" #문자


#a의 값을 다른곳에 저장하고 싶다. 
a2 = a
a = 123
print(a) #123
print(a2) #11


c = [1,2,3] #리스트 
c2 = c[:] #슬라이싱 할거여 처음부터 끝까지 -> 새로운 리스트를 가져올거임 


c[0] = 100
print(c) #[100,2,3]
print(c2) #[1,2,3]

print()

d = [1,2,3]

d2 = d

d = 100
print(d) #100
print(d2) #[1,2,3]

mat = [[0,0],
       [0,0]
]

mat2 = mat[:]

mat[0][0] = 100
print(mat) #[[100, 0], [0, 0]]
print(mat2) #[[100, 0], [0, 0]]

from copy import deepcopy

deepcopy()

# 1. 1차원 리스트는 슬라이싱 활용한 얕은 복사 
# 2. 다차원 리스트는 deepcopy 사용 

