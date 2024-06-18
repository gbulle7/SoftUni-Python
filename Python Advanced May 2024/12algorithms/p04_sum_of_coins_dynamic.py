def min_coins(target, coins):
    # Initialize a list to store the minimum number of coins needed for each amount up to the target
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the sum 0

    # Compute the minimum coins required for all values from 1 to target
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[target] is still float('inf'), it means it's not possible to form the target sum with the given coins
    if dp[target] == float('inf'):
        return "No solution with the given coin denominations"

    # Backtrack to find the coins used
    result = []
    while target > 0:
        for coin in coins:
            if target - coin >= 0 and dp[target] == dp[target - coin] + 1:
                result.append(coin)
                target -= coin
                break

    return result


# Example usage
target_sum = 17
available_coins = [10, 4, 7, 3, 1]
result = min_coins(target_sum, available_coins)

if isinstance(result, list):
    print(f"Minimum number of coins required: {len(result)}")
    print(f"Coins used: {result}")
else:
    print(result)
