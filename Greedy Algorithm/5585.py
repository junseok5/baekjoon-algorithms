price = int(input())
coins = [500, 100, 50, 10, 5, 1]
change = 1000 - price

change_coin_num = 0

for coin in coins:
    if change >= coin:
        num = change // coin
        change = change - coin * num
        change_coin_num = change_coin_num + num

print(change_coin_num)
