def fact(n):
    if n == 1: #멈추는 조건 
        return 1
    result = fact(n-1) * n
    return result

# def fibo(n):
#     if n<=2:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# # 1 1 2 3 5 8
# print(fibo(5))




def fino(n):
    lst = [0,1,1]

    for _ in range(n-2):
        lst.append(sum(lst[-2:]))
        return lst[n]


def fibo(n):
    lst = [0,1,1]
    if lst[n]:
        return lst[n]
    else:
        lst[n] = fibo(n-1) + fibo(n-2) #lst[n]이 없으면 만들어서 만들어줌 
        return lst[n]

print(fibo(3))

lst = [0]*(n+1)
lst[1] = 1
lst[1] = 1
   
# def fibo(n):
#     if not lst[n]:
#         lst[n] = fibo(n-1) + fibo(n-2)
#     return lst[n]


