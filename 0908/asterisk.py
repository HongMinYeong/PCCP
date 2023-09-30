a, b = [1, 2]
print(a, b)

a, *b = [1, 2, 3, 4]
print(a, b)

lst = [1, 2, 3, 4]
print(lst)
print(1, 2, 3, 4)
print(*lst)

def func(*args):
    s = 0
    for num in args:
        s += num
    return s

print(func(1, 2, 3, 4))

def func2(*args, **kwargs):
    print(args)
    print(kwargs)
    return

func2(1, 2, 3, 4, a=3, b=5, c=7)
