# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

path = []
N = 3

def run(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1, 4):
        path.append(i)
        run(lev + 1)
        path.pop()

run(0)
