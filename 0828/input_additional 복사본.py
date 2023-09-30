input_str = "배근표10 권이혁5 강산30 승희엄마100"
input_str = input_str.split()

print(input_str)
dic = dict()
for single_str in input_str:
    for index in range(len(single_str)):
        if single_str[index].isnumeric():
            name = single_str[:index]
            num = int(single_str[index:])
            dic[name] = num
            break
print(dic)

    # for single_chr in single_str:
    #     if single_chr.isnumeric():
    #         썸 동작
# 답이 중요한게 아니라 문제에 어떻게 접근을 해야 하는지 생각하는게 중요합니다!