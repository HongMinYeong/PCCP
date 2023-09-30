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

def perm(depth):
    # print(check)
    if depth == n:
        print(select)
        # print()
        return

    for i in range(len(lst)):
        if not check[i]:
            select[depth] = lst[i]
            check[i] = 1
            perm(depth + 1)
            check[i] = 0
perm(0)



