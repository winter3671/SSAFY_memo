# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition1(left, right):
    pivot = arr[left]  # 피벗을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right
            
    while i <= j:
        while i <= j and arr[i] <= pivot:  # i 는 pivot 보다 큰 값을 검색(작거나 같으면 i += 1)
            i += 1
        
        while i <= j and arr[j] >= pivot:  # j 는 pivot 보다 작은 값을 검색(크거나 같으면 j -= 1)
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

arr = [3, 1, 2, 5, 6, 7, 9, 8, 4]