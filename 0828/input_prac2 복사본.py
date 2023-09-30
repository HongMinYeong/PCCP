import sys

sys.stdin = open('input2.txt')

n = int(input())

matrix = []
dic = dict()
for _ in range(n):
    name, age = input().split()

    matrix.append([name, int(age)])

    # dic[name] = int(age)
    dic[name] = {'age': int(age)}

print(matrix)
print(dic)