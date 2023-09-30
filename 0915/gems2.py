from collections import  defaultdict
def solution(gems):
    gems_set = set(gems)
    gems_type_num = len(gems_set)
    gem_dic = defaultdict(int)
    l = 0
    short_range = len(gems)
    for r in range(len(gems)):
        gem_dic[gems[r]] += 1
        while len(gem_dic) == gems_type_num:
            if short_range > r - l:
                short_range = r - l
                answer = [l + 1, r + 1]
            # l이 움직일 차례야.
            # l도 1씩 커지면서 움직입니다.
            gem_dic[gems[l]] -= 1
            if gem_dic[gems[l]] == 0:
                del gem_dic[gems[l]] # gems_dic의 개수를 명확히 하기 위해서
            l += 1
    return  answer
s = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	)
print(s)







