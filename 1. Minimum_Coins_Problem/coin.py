def fewest_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    # BASE CASE
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount]!= float('inf') else -1
    

# Input Handling
c = list(map(int,input().split())) # Availabe coins
n = int(input())  # Amount
print(fewest_coins(c,n))