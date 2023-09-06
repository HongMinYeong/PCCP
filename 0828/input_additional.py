# import re
#
# input_str = "배근표10 권이혁5 강산30 승희엄마100"
# tokens = input_str.split()
#
# # Using regular expressions to extract names and numbers
# pattern = re.compile(r'([가-힣]+)(\d+)')
# matches = pattern.findall(input_str)
#
# # Creating a dictionary
# result_dict = {name: int(number) for name, number in matches}
#
# print(result_dict)

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
    #
