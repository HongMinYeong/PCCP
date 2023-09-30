def fact(n):

    if n == 1:
        return 1

    result = fact(n-1) * n
    return result

print(fact(5))




def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)


def fibo(n):
    lst = [0, 1, 1]

    for _ in range(n-2):
        lst.append(sum(lst[-2:]))
    return lst[n]


lst = [0]*(n+1)
lst[1] = 1
lst[2] = 1
def fibo(n):
    if not lst[n]:
        lst[n] = fibo(n-1) + fibo(n-2)
    return lst[n]



