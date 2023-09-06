# 딕셔너리의 구조 ⇒  `{ key : value }`
#
# key 값으로 접근해 value 값을 얻을 수 있습니다. 해쉬 자료구조로써 탐색이 O(1)로 매우 빠릅니다.
#
# 없는 key 값에 접근하려 하는 경우 에러가 발생합니다.

# user_info = {'name': 'alex'}
# print(user_info['name']) # alex
# # print(user_info['age']) # KeyError: 'age'
#
# # 기본적인 추가와 수정
# user_info = dict()
# user_info['name'] = 'alex'
# print(user_info) # {'name': 'alex'}

# get 메서드를 활용해 key값에 접근, value값을 얻을 수 있습니다.
# 직접 접근과 다르게 없어도 에러가 발생하지 않으며, 만약 찾지 못하는 경우 반환할 기본 값을 지정할 수 있습니다.
# 기본 값을 지정하지 않으면 찾지 못하는 경우 None을 반환합니다.
user_info = {'name': 'alex'}
print(user_info.get('name')) # alex
print(user_info.get('age', '발견하지 못함')) # 발견하지 못함

#join
word = ['p','y','t','h','o','n']

# result=""
# for x in word:
#     result +=result + x


# word.join("")

#zip
# zipped_lst = zip([
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
# ])
#
# print(zipped_lst) #<zip object at 0x7fe0cdc24fc0>
# print(list(zipped_lst)) #형변환 ->

#map
# map(function 그자체가 들어가야함 , iterable)

lst = ['1','2','3','4']

#[1,2,3,4]-> ['1','2','3','4']로 바꾸는 함수 만들기
def times_10(x):
    return x*10

result = []
for i in [1,2,3,4]:
    result.append(str(i))


print(list(map(times_10,[1,2,3,4]))) #[10, 20, 30, 40]


# mapped_lst=map(int,lst)
#
# print(list(mapped_lst))