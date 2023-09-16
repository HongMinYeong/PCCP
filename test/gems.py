def solution(gems):
    gems_set = set(gems)
    gems_type_num = len(gems_set)
    #시작 인덱스에 대해서 걔를 포함하는 오른쪽 set을 모아놓을꺼에요
    gems_set_list = [set() for _ in range(len(gems))]

    pointer = 0
    while True:
        #작은 개수부터 천천히 갈 것이기 때문에 -> 발견하면 멈추자@
        for i in range(len(gems)):
            if i + pointer <len(gems):
                gems_set_list[i].add(gems[i + pointer])
                if len(gems_set_list[i]) == gems_type_num:
                    return [i+1,i+pointer+1]
        pointer += 1

    answer = []
    return answer

s = solution(["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"])
print (s)