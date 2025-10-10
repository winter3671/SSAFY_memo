# 완전탐색으로 부분집합 구하기
def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return
    
    # 부분집합에 포함 시키는 경우
    recur(cnt + 1, subset + [name[cnt]])
    # 포함 시키지 않는 경우
    recur(cnt + 1, subset)

name = ['A', 'B', 'C']
recur(0, [])