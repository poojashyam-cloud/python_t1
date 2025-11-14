def count_ways_dp(coins, n):
    combinations = [0] * (n+1)
    combinations[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            combinations[i] += combinations[i - coin]
    return combinations[n]

# Example usage:
coins = [1,2, 5, 10]
n = int(input("Enter any rupees : "))
print(count_ways_dp(coins, n))