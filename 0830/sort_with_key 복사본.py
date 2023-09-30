lst = [[1, 3], [5, 2], [2, 1],  [7, 8]]


def func(x):
    return x[1]

lst.sort(key=func)

print(lst)

def func(x):
    return sum(x)

lst.sort(key=func)

print(lst)