# list, queue, stack

from collections import deque , defaultdict

queue = deque()
# queue, stack

queue.append(1)
queue.append(2)
queue.append(3)
queue.appendleft(4)
queue.pop()
queue.popleft()
print(queue)

print(queue)

a = [1, 2, 3, 4, 5]

print(a[:3])

b = deque(a)

print(b)

# print(b[:3])


dic = defaultdict(int)

dic['a'] += 1
print(dic)

normal_dic = dict()
#
# normal_dic['a'] += 1
#
#
#
#


