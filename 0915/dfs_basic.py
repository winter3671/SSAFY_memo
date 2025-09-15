def dfs(node):
    print(node, end = " ")

    # node 로 부터 갈 수 있는 노드들을 확인하고, 한 곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 x
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)