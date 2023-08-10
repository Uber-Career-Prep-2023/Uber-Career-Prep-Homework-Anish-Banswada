# Name : Anish Banswada

# Strategy :Tabulation

# Time Taken : 25 minutes

# Assumptions : None

# Space Complexity : O(n)

# Time Complexity : O(n)

# Function 
def minStairs(steps):
    if len(steps) <= 2:
        return min(steps)
    dp = [0] * len(steps)
    dp[0] = steps[0]
    dp[1] = steps[1]
    for i in range(2,len(steps)):
        dp[i] = min(dp[i-1],dp[i-2]) + steps[i]
    return min(dp[-1],dp[-2])


# Main

if __name__ == "__main__":
    assert minStairs([4, 1, 6, 3, 5, 8]) == 9
    assert minStairs([11, 8, 3, 4, 9, 13, 10]) == 25
    assert minStairs([2,1,5,1,9,1]) == 3
    assert minStairs([5,19,2,4,1,3,6,7]) == 14
    print('Testing completed')
   
 