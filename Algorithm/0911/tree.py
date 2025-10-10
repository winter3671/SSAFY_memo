arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10]

# 그래프처럼 저장하는 방식
nodes = [[] for _ in range(10)]

for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

def order(node):
    if node == None:
        return
    
    order(nodes[node][0])
    order(nodes[node][1])
    print(node, end = ' ')  # 후위순회

order(1)