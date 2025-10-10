import sys
sys.stdin = open("input.txt")

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

def recur(y, x, num):
    if len(num) == 7:
        result.add(num)
        return
    
    for dx, dy in zip(delta_x, delta_y):
        nx = x + dx
        ny = y + dy

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue
            
        recur(ny, nx, num + matrix[ny][nx])


T = int(input())
for tc in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    for sy in range(4):
        for sx in range(4):
            recur(sy, sx, matrix[y][x])

    print(f'#{tc} {len(result)}')