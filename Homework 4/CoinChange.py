# Name : Anish Banswada

# Strategy : Memoization

# Time Taken : 40 minutes

# Assumptions : None

# Space Complexity : O(n*amount)

# Time Complexity : O(n*amount)

# Function 
def coinChange(amount,coins):
    dp = {}
    def dfs(i,amount):
        if(i,amount) in dp:
            return dp[(i,amount)]
        if i >= len(coins):
            return 0
        if amount == 0:
            return 1
        if coins[i] > amount:
            dp[(i,amount)] = dfs(i+1,amount)
        else:
            dp[(i,amount)] = dfs(i+1,amount) + dfs(i,amount-coins[i])
        return dp[(i,amount)]
    return dfs(0,amount)

# Main

if __name__ == "__main__":
    print(coinChange(20,[2,5,10]))





 