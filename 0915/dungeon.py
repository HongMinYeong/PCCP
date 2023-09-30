
# def func(k, dungeons, visited, cnt):
#     answer_lst = [cnt]
#     for idx, dungeon in enumerate(dungeons):
#         if not visited[idx] and k >= dungeon[0]:
#             visited[idx] = 1
#             tmp_cnt = func(k - dungeon[1], dungeons, visited, cnt + 1)
#             answer_lst.append(tmp_cnt)
#             visited[idx] = 0
#     return max(answer_lst)

answer = 0
def func(k, dungeons, visited, cnt):
    global answer
    if answer < cnt:
        answer = cnt

    for idx, dungeon in enumerate(dungeons):
        if not visited[idx] and k >= dungeon[0]:
            visited[idx] = 1
            func(k - dungeon[1], dungeons, visited, cnt + 1)
            visited[idx] = 0



def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer = func(k, dungeons, visited, 0)
    return answer




