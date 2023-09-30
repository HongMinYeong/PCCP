# lst = [1, 2, 3]
#
# # lst.append(원소(더하고자 하는 데이터))
# output = lst.append(4)
#
# print(lst)
# print(output)
# print()
#
# output = lst.pop()
#
# print(lst)
# print(output)
#
#
#
#
# lst2 = [1, 5, 3, 6, 2]
#
# output = lst2.sort()
#
# print(lst2)
# print(output)
# print()
#
# lst2 = [1, 5, 3, 6, 2]
#
# output = sorted(lst2)
#
# print(lst2)
# print(output)


nums = [3, 5, 1, 4, 2]

inserted_nums = [3, 4, 5]

# result = [3, 3, 4, 5, 5, 1, 4, 2]

# 첫번째 (안됨)
# nums.insert(1, inserted_nums)

# 두번째
# for num in inserted_nums[::-1]:
#     nums.insert(1, num)

# 세번째
#
# inserted_nums.reverse()
# for num in inserted_nums:
#     nums.insert(1, num)

# 네번째
# idx = 1
# for num in inserted_nums:
#     nums.insert(idx, num)
#     idx += 1

# 다섯번째
# nums = nums[:1] + inserted_nums + nums[1:]

# 여섯번째
# nums[1:1] = inserted_nums
print(nums)





#join
# word = ['p', 'y', 't', 'h', 'o', 'n']
#
#
#
# result = ""
# for x in word:
#     result += result + x
#
#
# "".join(word)
#
#
# word.join("")


# zip

zipped_lst = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(zipped_lst)

print(list(zipped_lst))


# map

# map(func, iterable)

lst = ['1', '2', '3', '4']

int_lst = [1, 2, 3, 4]


mapped_lst = map(int, lst)

print(list(mapped_lst))

lst = []

lst.append(str(1))
lst.append(str(2))
lst.append(str(3))
lst.append(str(4))

for i in [1, 2, 3, 4]:
    lst.append(str(i))

def times_10(x):
    return x * 10

print(list(map(times_10, [1, 2, 3, 4])))

a = times_10












