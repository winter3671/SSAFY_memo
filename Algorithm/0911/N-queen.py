# 종료 조건: N개의 행을 모두 고려하면 종료
# 가지의 수: N개의 열
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visited[i][col]:
            return False
        
    # 2. 좌상단 대각선에 놓은 적이 있는가?
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        
        i -= 1
        j -= 1

    # 3. 우상단 대각선에 놓은 적이 있는가?
    i, j = row-1, col-1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        
        i -= 1
        j += 1


def recur(row):
    if row == N:
        return
    
    for col in range(N):
        # 가지치기 : 같은 열을 못 고르도록
        # --> 유망하지 않은 케이스를 모두 삭제(세로, 대각선)
        if check(row, col) is False:
            continue

        visited[row][col] = 1
        recur(row + 1)
        visited[row][col] = 0

N = 4
answer = 0
visited = [[0] * N for _ in range(N)]
recur(0)

print(f'N = {N} / answer = {answer}')