lst = []
a = [1,0,0,1]
b = [1,1,1,1]
c = [1,0,1,0 ]

lst.append(a)
lst.append(b)
lst.append(c)


from pprint import pprint

n = 2
gugudan = []
for n in range(10):
    ndan = []
    n = 2
    for i in range(1, 10):
        ndan.append( n * i )
    gugudan.append(ndan)

pprint(gugudan)



# 2  # 문제의 개수

# # 처번째 문제
# 4 5 2  # 사람수, 신고수, k
# muzi frodo apeach neo # 사람 목록
# # 여기서부터는 신고 목록
# muzi frodo
# apeach frodo
# frodo neo
# muzi neo
# apeach muzi

# # 두번째 문제
# 2 4 3 # 사람수, 신고수, k
# con ryan
# ryan con
# ryan con
# ryan con
# ryan con