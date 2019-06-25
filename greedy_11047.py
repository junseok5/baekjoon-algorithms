N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

needed_coins = 0

for i in range(1, N + 1):
    max_coin = coins[-i]

    if K >= max_coin:
        num = K // max_coin
        K = K - max_coin * num
        needed_coins = needed_coins + num

print(needed_coins)
