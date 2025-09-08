'''
arr = [1, 2, 3, 4]

# i: 0 ~ 2^n == i번째 부분집합
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()
'''

arr = ['A', 'B', 'C']

def get_sub(tar):
    print(f'target = {tar}', end='/')
    for i in range(len(arr)):
        # 0x1로 적는 이유: 비트연산임을 명시하는 권장 방법이기 때문
        if tar & 0x1:      # 가장 우측 비트를 체크   
            print(arr[i], end = ' ')
        tar >>= 1

for target in range(1 << len(arr)):
    get_sub(target)
    print()