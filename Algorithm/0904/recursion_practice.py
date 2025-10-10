def KFC(n):
    if n == 4:  # 종료조건 : 4
        return

    print(n)
    KFC(n+1)
    KFC(n+1)
    print(n)

KFC(0)

#  maximum recursion depth exceeded