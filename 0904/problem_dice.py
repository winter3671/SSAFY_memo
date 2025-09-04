path = []
result = 0

def recur(cnt):
    global result

    if sum(path) > 10:
        return

    if cnt == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()

recur(0)

#--------------------------------------

def recur(cnt, total):
    global result

    if total > 10:
        return

    if cnt == 3:
        result += 1
        return

    for num in range(1, 7):
        recur(cnt + 1, total + num)


result = 0
recur(0, 0)