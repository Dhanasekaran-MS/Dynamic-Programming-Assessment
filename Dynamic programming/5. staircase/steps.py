def distinct_ways(steps):
    if steps == 0:
        return 0
    if steps == 1:
        return 1
    
    dp = [0] * (steps+1)
    # base cases
    dp[1]=1
    dp[2]=2
    
    for i in range(3, steps+1):
        # Finding the distinct ways by adding the ways of previous two steps
        dp[i] = dp[i-1] + dp[i-2]
    return dp[steps]

# Input Handling
inp = int(input())

print(distinct_ways(inp))