from collections import deque

def bfs(start_node):
    # q는 다음에 방문해야 할 노드들(후보열, 대기열)
    q = deque([start_node])  # 시작점을 queue에 넣고 시작

    while q:
        # 1. 가장 앞의 노드를 뽑음
        # 2. 해당 노드에서 갈 수 있는 노드들을 queue에 넣음
        now = q.popleft()

        print(now, end = " ")

        for next_node in graph[now]:
            if visited[next_node]:
                continue

        visited[next_node] = 1
        q.append(next_node)


V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (V + 1)
visited[1] = 1
bfs(1)