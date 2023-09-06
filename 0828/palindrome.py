word = '수박이수박이다'
# word = '수박수'
#word 뒤집기
reversed_word = word[::-1]
print(reversed_word)

if(word == reversed_word):
    print('회문이다')

else:
    print('회문이 아님')

#2번재 -> 처음과 끝 비교

#3번째 -> index로 접근하거나
n = len(word) #7
i = 0
j = n-1

print(word[i],word[j])

for _ in range(n):
    if word[i] != word[j]:
        print('회문이 아님')
        break #같지 않는 경우에 멈춤 , 멈추지 않았을 때는 else 실행
    print('i는 >> ',i,'j는 >>',j)
    i += 1
    j -= 1
else:
    print("회문이당")

def palindrome_1(word):

    n = len(word)  # 7
    i = 0
    j = n - 1

    print(word[i], word[j])

    for _ in range(n):
        if word[i] != word[j]:
            return False
        print('i는 >> ', i, 'j는 >>', j)
        i += 1
        j -= 1
    else:
        return print("회문이당")

def palindrome_2(word):
#n이 홀수일때는 2로 나눴을때 n//2-1까지만 반복하면됨
#n이 짝수일때는 2로 나눴을 때 n//2 -1 까지만
# 근데 +1 해야 할때가 있음
    n = len(word)  # 7
    i = 0
    j = n - 1

    print(word[i], word[j])

    for _ in range(n//2): #n//2 -1 까지
        if word[i] != word[j]:
            return False
        print('i는 >> ', i, 'j는 >>', j)
        i += 1
        j -= 1
    else:
        return print("회문이당")

def palindrome_3(word):
    n = len(word)
    i = 0
    j = -1-i

    print(word[i], word[j])

    for _ in range(n//2): #n//2 -1 까지
        if word[i] != word[-1-i]:
            return False
        i += 1
    else:
        return print("회문이당")

palindrome_3('수박이박수')
palindrome_3('박수박수')
palindrome_3('다시합창합시다')