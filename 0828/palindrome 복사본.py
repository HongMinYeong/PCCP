# word = '수박이수박이다'
# revered_word = word[::-1]
#
#
# print(revered_word)
#
# if word == revered_word:
#     print('회문이다')
# else:
#     print('회문이 아니다')


word = '수박이수박이다'
n = len(word)
i = 0
j = n - 1

for _ in range(n):
    if word[i] != word[j] :
        print('회문이 아니다')
        break
    i += 1
    j -= 1
else:
    print('회문이다')

def palindrome_1(word):
    n = len(word)
    i = 0
    j = n - 1

    for _ in range(n):
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    else:
        return True

print(palindrome_1('수박이박수'))
print(palindrome_1('박수박수'))
print(palindrome_1('다시합창합시다'))

def palindrome_2(word):
    n = len(word)
    i = 0
    j = n - 1

    for _ in range(n//2):
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    else:
        return True


def palindrome_3(word):
    n = len(word)
    i = 0
    for _ in range(n//2):
        if word[i] != word[-1 - i]:
            return False
        i += 1
    else:
        return True

# j는 안바뀜
i = 0
j = -1 - i

for _ in range(3):
    i += 1
    print(i, j)




