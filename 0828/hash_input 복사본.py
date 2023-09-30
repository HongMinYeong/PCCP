import sys

sys.stdin = open("01_Hashing_report_result.txt")
# test_cases = int(input())
for case in range(2):
    n, m, k = map(int,input().split())
    name_list = input().split()
    matrix = []

    # for _ in range(m):
    #     tmp_list = input().split()
    #     matrix.append(tmp_list)

    matrix = [input().split() for _ in range(m)]
    print(matrix)

    for person in matrix:
        reporter, reportee = person
        # print(reporter)
        print(f'{reporter}가 {reportee}를 신고했어요!')
        # print(reporter, '가 ', reportee, '를 신고해써요!', end="")
        # print()









