# 1. 분할
# 2. 정복(정렬) & 병합
def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

def merge_sort(li):
    if len(li) == 1:
        return

    # 절반씩 분할하여 출력
    mid = len(li) // 2
    left = li[:mid] 
    right = li[mid:]
    
    left_list = merge_sort(left)
    right_list = merge_sort(right)
    
    merge_list = merge(left_list, right_list)
    return merge_list
    



arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)