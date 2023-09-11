# 로무토 짱
a = [6, 3, 7, 2, 5, 8, 11, 13]
# pivot 을 기준으로 왼쪽오른쪽 정렬 

def lomuto(low, high):
    def lomuto_partition(low, high): #low,hight일때 pivot 만드는 녀석 
        pivot = a[high]  # 로무토는 맨 오른쪽을 초기 피봇으로 일단 삼는다
        left = low  # 우선 제일 왼쪽은 low 값으로 초기화 

        for right in range(low, high):  # right => 이동하는 포인터
            if a[right] < pivot:  # 만약 돌아다니면서 피봇보다 작은걸 구한 경우?
                a[left], a[right] = a[right], a[left]  # left,  right 위치 스왑
                left += 1  # 칸막이 한칸 이동

        a[left], a[high] = a[high], a[left]  # 솎아내는거 다 끝나면 칸막이 위치와 맨 오른쪽 피봇값을 스왑
        print(a,pivot)
        return left  # 칸막이 인덱스를 뱉음

    if low < high:
        pivot = lomuto_partition(low, high)  # 뱉어진 칸막이를 기준으로 반땡
        lomuto(low, pivot-1) # 새로운 high -> pivot -1 
        lomuto(pivot+1, high)


lomuto(0, len(a)-1)
print(a)

# 호어 성님!  -> l과 r이 서로 반대로 이동함 

lst = [9,3,7,2,5,8,11,13]

def hoare(low, high):
    def hoare_partition(low, high):
        pivot = (low + high) // 2
        L = low
        R = high

        while L < R:
            while lst[L] < lst[pivot] and L < R:  # 피봇보다 작으면 그다음걸 봐라
                L += 1  # 왼쪽 영역은 피봇보다 큰걸 찾는게 목표니까.
            while lst[R] >= lst[pivot] and L < R:
                R -= 1
            if L < R:  # 2번 왼쪽에선 피봇보다 큰걸 찾았고 오른쪽에서도 피봇보다 작은걸 적당히 찾은 경우?
                if L == pivot:  # 3번 이건 둘이 완전 쫍아졌을때의 이야기
                    pivot = R
                lst[L], lst[R] = lst[R], lst[L]  # 2-1번 그러면 L, R 포인터 위치 스왑 피봇의 왼쪽에서 큰걸 오른쪽으로 토스하고 오른쪽에서 작은걸 왼쪽으로 토스

        lst[pivot], lst[R] = lst[R], lst[pivot]  # 1 번 둘이 별탈없이 만나버린 경우라면 피벗과 R 포인터 위치를 교환한다.
        print(lst,pivot)
        return R

    if low < high:
        pivot = hoare_partition(low, high)
        hoare(low, pivot-1)
        hoare(pivot+1, high)

hoare(0, len(lst)-1)
print(lst)

# sudo code 
# pivot:lst[-1]
# left = [x for x in lst if x < pivot]
# right = [x for x in lst if x > pivot]
# lst = left + [pivot] + right