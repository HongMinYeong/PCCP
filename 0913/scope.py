a = 1
b = [1, 2, 3]

print(a)
def func():
    # 동작들을 기능 단위로 묶을 수 있게 되었어요.
    global  a
    a = 3
    b = [4, 5, 6]
    b[1] = 100


func()
print(a)
print(b)


def func():
    # 동작들을 기능 단위로 묶을 수 있게 되었어요.
    a = 3
    # b = [4, 5, 6]
    b[1] = 100



def func(a, b):
    # 동작들을 기능 단위로 묶을 수 있게 되었어요.
    a = 3
    # b = [4, 5, 6]
    b[1] = 100
    return a, b

a,b = func(a, b)
# func()






