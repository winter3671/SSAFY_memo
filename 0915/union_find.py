# 각 집합을 만들어주는 함수
def make_set(n):
    # 1~n 까지의 원소가 "각자 자기 자신이 대표자로 설정"
    parents = [i for i in range(N + 1)]
    return parents

# 집합의 대표자를 찾는 함수
def find_set(x):
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == parents[x]:
        return x
    
    # x의 부모노드를 기준으로 다시 부모를 검색
    find_set(parents[x])

# 두 집합을 합치는 함수
def union(x, y):
    # x, y의 대표자를 검색
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 만약 이미 같은 집합이라면 합칠 필요가 없음
    if rep_x == rep_y:
        return

    # # 더 작은쪽으로 연결
    # if rep_x < rep_y:
    #     parents[rep_y] = rep_x
    # else:
    #     parents[rep_x] = rep_y

    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        # rank가 동일하면 한쪽으로 병합하고, 대표자의 rank를 + 1
        parents[rep_y] = rep_x
        ranks[rep_x] += 1    

N = 6
parents, ranks = make_set(N)

union(2, 4)
union(4, 6)