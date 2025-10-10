import sys
sys.stdin = open('input.txt', "r")

from heapq import heappush, heappop

# 특정 정점 기준으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 감
# 작은 노드를 먼저 꺼내기 위해 heapq를 활용
def prim(start_node):
    pq = [(0, start_node)]  # (가중치, 노드) 형태
    MST = [0] * V  # visited 와 동일
    min_weight = 0   # 최소 비용

    while pq:
        weight, node = heappop(pq)  # 가장 작은 가중치

        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue

        MST[node] = 1     # node로 가는 최소 비용 선택
        min_weight += weight     # 누적합 추가

        for next_node in range(V):
            # 갈 수 없으면 continue
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 continue
            if MST[next_node]:
                continue

            # 원래 BFS 에서는 여기서 방문 처리
            heappush(pq, (graph[node][next_node], next_node))


    return min_weight

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]  # 인접행렬

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight


result = prim(0)   # 출발 정점과 함께 시작
                    # 출발 정점을 바꾸어도 그래프는 동일하게 나옴
print(f'최소 비용 = {result}')