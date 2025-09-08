# [문제] 동전의 최소 개수
# 규칙: 큰 동전부터 나누기
coin_list = [100, 50, 500, 10]
target = 1730
cnt = 0

# Greedy 문제의 단골 손님
# 정렬 연습(sort)
# list.sort() vs sorted() 정리하기
coin_list.sort(reverse=True)
# print(coin_list)  # [500, 100, 50, 10]

for coin in coin_list:
    possible_cnt = target // coin   # 현재 동전으로 가능한 최대 수
    result += possible_cnt          # 정답에 더해주고
    target -= coin * possible_cnt   # 금액을 빼준다.

print(result)