import sys

sys.stdin = open('input2.txt')
n = int(input()) #3 -> 3번 반복한다.

matrix = []

# for _ in range(n):
#     matrix.append(input().split())


# for _ in range(n):
#     #두번쨰 인자는 int 로 받고 싶어
#     name,age = input().split()
#     matrix.append([name,int(age)])

dic = dict()
for _ in range(n):
    #두번쨰 인자는 int 로 받고 싶어
    name,age = input().split()
    matrix.append([name,int(age)])

    # dic[name] = int(age)
    dic[name] = {'age' : int(age)}
print(matrix)
print(dic)
