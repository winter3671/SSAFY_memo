import sys
sys.stdin = open('input.txt')

def find_set(x):
    if x == parents[x]:
        return x
    
    # 기본 코드
    # return find_set(parents[x])

    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:    # 사이클 발생
        return

    # 일정한 규칙으로 병합(더 작은 수로)
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

# 가중치 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택
# 사이클이 발생하면 선택 x
# MST가 완성될 때까지(V-1개를 선택할 때까지)
cnt = 0      # 현재까지 선택한 간선의 수
result = 0      # 가중치의 합

parents = [i for i in range(V)]   # make_set()

for u, v, w in edges:
    # 사이클이 아니라면 연결(같은 집합으로 만듦)
    # cnt += 1
    # cnt 가 V - 1이면 종료
    if find_set(u) != find_set(v):     # 사이클이 아니라면
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            continue

print(result)