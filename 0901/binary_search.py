#이진 탐색 
#정렬이 되었다는 가정하에 

lst = list(range(1,9))


def binary_search(s,e,target): #리스트 왼쪽 오른쪽 기준 잡기 -> 가운데 잡기 위해서 
    mid = (s + e)//2
    if lst[mid] == target:
        print('찾았다!') 
        return True
    #mid가 target보다 작다면 
    if lst[mid] > target: #target이 가운데보다 작은 경우 
            return binary_search(s,mid -1 ,target)
    elif lst[mid] < target: #target이 가운데보다 클 경우 
        return binary_search(mid+1,e,target)