def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr)-1      # 검색 끝점

    while left <= right:    # 교차가 된다면 탐색에 실패한 것
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid   # mid 위치에 존대한다면 return
        
        # target 보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid - 1
        # target 보다 정답이 오른쪽에 있는 경우
        else:
            left = mid + 1

    return -1, cnt




arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에만 적용 가능
arr.sort()

binary_search_while(9)  # 처음과 끝을 전달