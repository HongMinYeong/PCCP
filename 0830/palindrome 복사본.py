def palindrome_3(word):
    n = len(word)
    i = 0
    fail_count = 0
    for _ in range(n):
        # 다를때마다
        if word[i] != word[-1 - i]:
            fail_count += 1
        i += 1
    if fail_count > 0:
        return False
    else:
        return True


def palindrome_3(word):
    n = len(word)
    i = 0
    success_count = 0
    for _ in range(n):
        # 같을 때 마다
        if word[i] == word[-1 - i]:
            success_count += 1
        i += 1
    if success_count == n:
        return True
    else:
        return False


n = len(word)
i = 0
status = True

for _ in range(n):
    # 같을 때 마다
    if word[i] != word[-1 - i]:
        status = False
    i += 1


print(status)



















