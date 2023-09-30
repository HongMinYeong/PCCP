lst = [1, 2, 3, 4, 5]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                print(i, j, k)

lst = ['a', 'b', 'c', 'd', 'e']
m = len(lst)

n = 3
select = [0] * n

check = [0] * len(lst)
lst2 = []
def perm(depth):
    # print(check)
    if depth == n:
        print(select)
        lst2.append(select[:])
        # print()
        return

    for i in range(len(lst)):
        if not check[i]:
            select[depth] = lst[i]
            check[i] = 1
            perm(depth + 1)
            check[i] = 0
# perm(0)
# print(lst2)


# 중복 순열
lst = ['a', 'b', 'c', 'd']
m = len(lst)

n = 3
select = [0] * n

def dup_perm(depth):
    if depth == n:
        print(select)
        return

    for i in range(len(lst)):
        select[depth] = lst[i]
        perm(depth + 1)
# dup_perm(0)

# 조합

lst = ['a', 'b', 'c', 'd', 'e']
n = 3
select = [0]*n

def combination(depth, index):
    if depth == n:
        print(select)
        return
    if index == len(lst):
        return
    select[depth] = lst[index]

    combination(depth+1, index+1)
    combination(depth, index + 1)

# combination(0, 0)
print(select)



from itertools import combinations, permutations

lst = list(combinations([1, 2, 3, 4], 2))
lst2 = list(permutations([1, 2, 3, 4], 3))
print(lst)
print(lst2)









