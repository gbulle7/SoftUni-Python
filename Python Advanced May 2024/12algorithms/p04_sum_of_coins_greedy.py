def choose_coins(coins, target):
    coins.sort(reverse=True)
    index = 0
    used_coins = {}

    while index < len(coins) and target != 0:
        count_coins = target // coins[index]
        target %= coins[index]
        if count_coins > 0:
            used_coins[coins[index]] = count_coins
        index += 1

    if target != 0:
        return 'Error'
    else:
        result = f'Number of coins to take: {sum(used_coins.values())}\n'
        for coin, count in used_coins.items():
            result += f'{count} coin(s) with value {coin}\n'
        return result.strip()


coins_input = list(map(int, input().split(', ')))
target_sum = int(input())
print(choose_coins(coins_input, target_sum))
