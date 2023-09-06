 #  list = [1,2,3] 가능은 하지만 List라는 메소드가 이미 있으므로 지양해야 한다. (예약어 지양)
############################################################################
#method1) .append()
lst = [1, 2, 3]
# list.append(원소 (더하고자 하는 데이터))
output = lst.append(4)

print (lst) #[1,2,3,4]
print(output) #None 리스트는 어떤 결과가 아님
############################################################################
#.method2) .pop(index)
# lst.pop()
#
# print(lst) #[1, 2, 3]

output = lst.pop()

#뺀값을 출력한다.
print(output) #4
#파이썬의 list는 길이가 정해져있지 않음
############################################################################
#method3) .sort()
#   ->리스트를 정렬하는 메서드
#정렬후 원래 리스트값을 잃어버림

lst2 = [1,5,3,6,2]
output = lst2.sort()

print(lst2) #[1, 2, 3, 5, 6]
print(output) #None

############################################################################
# +) sorted()함수!
#=> 정렬 전과후의 list를 둘 다 가지고있음
lst2 = [1,5,3,6,2]

output= sorted(lst2)

print(lst2) #[1, 5, 3, 6, 2]
print(output) #[1, 2, 3, 5, 6]

# [함수의 특징] => input이 들어가면 output이 나온다.
############################################################################
a = 1
lst11=[1,2,3]
def func(lst):
    # global a    #응 바깥에 영향 미칠게~ 라는 뜻
    # a = a+1
    lst[0]=10

    return lst11

func(lst11)

print(lst11)
# print(a)
############################################################################
#method4) .insert(인덱스위치,값)
#1번째 인덱스에 9 집어넣을게 ㅇㅇ
nums = [3, 5, 1, 4, 2]
nums.insert(1, 9)
print(nums) # [3, 9, 5, 1, 4, 2]

#slice 이용해서 3,4,5 1번째 인덱스에 넣기
numm = [3,5,1,4,2]
inserted_list = [3,4,5]
numm[1:1] = inserted_list

print(numm) #[3, 4, 5, 6, 1, 4, 2]

#=> list는 element를 가지는데 insert메서드는 리스트의 element로서
#  insert시키기 때문에 insert사용시 리스트채로 element에 넣는다.

#2번째 방법
# for num in inserted_list[::-1]:
#     numm.insert(1,num)
#
# print(numm)

#3번째 방법
# inserted_list.reverse()
# for num in inserted_list:
#     numm.insert(1,num)
#
# print(numm)

#4번째 방법
# idx = 1
# for num in inserted_list:
#     numm.insert(idx,num)
#     idx+=1
#
# print(numm)

#5번째 방법
# numm[:1]+inserted_list + numm[1:]
#
# print(numm)

