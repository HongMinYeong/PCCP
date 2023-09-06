#이거 코드 다시 
lst = [[1,3], [5,2], [2,1], [7,8]]

# 뒤에 기준으로 정렬
def func(x):
    return x[1]

# 앞에 기준으로 정렬
# def func2(x):
#     return x[0]

lst.sort(key=func)
# lst.sort(key=func2)


print(lst)
# 3,2,1,8기준으로 정렬 

def func(x):
    return sum(x)

lst.sort(key=func)

print(lst)

