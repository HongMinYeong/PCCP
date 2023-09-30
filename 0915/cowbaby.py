from collections import deque
def solution(s, e):
    if e < s:
        return s - e

    queue = deque()
    queue.append([s, 0])
    visited = [0] * 10001
    visited[s] = 1

    while queue:
        now, cnt = queue.popleft()
        if now == e:
            return cnt
        for next_location in [now-1, now+1, now+5]:
            if 1 <= next_location <= 10000 and not visited[next_location]:
                visited[next_location] = 1
                queue.append([next_location, cnt + 1])


#
#
# from collections import deque
# def solution(s, e):
#     if e < s:
#         return s - e
#
#     queue = deque()
#     queue.append(s)
#     visited = [0] * 10001
#     visited[s] = 1
#     answer = 0
#     while queue:
#         l = len(queue)
#         for _ in range(l):
#             now = queue.popleft()
#
#             for next_location in [now-1, now+1, now+5]:
#                 if next_location == e:
#                     return answer + 1
#                 if 1 <= next_location <= 10000 and not visited[next_location]:
#                     visited[next_location] = 1
#                     queue.append(next_location)
#         answer += 1
#
#





