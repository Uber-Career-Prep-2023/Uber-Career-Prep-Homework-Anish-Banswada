# Name : Anish Banswada

# Strategy : Tabulation

# Time Taken : 40 minutes

# Assumptions : None

# Space Complexity : O(n*m)

# Time Complexity : O(n*m)

# Function 
def largestSquare(matrix):
    r = len(matrix)
    c = len(matrix[0])
    dp = [[0]*(c+1) for i in range(r+1)]
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1]) + 1
                res = max(dp[i+1][j+1],res)
    return res

# Main

if __name__ == "__main__":
    assert largestSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 2
    assert largestSquare( [["0","1"],["1","0"]]) == 1
    assert largestSquare([["0"]]) == 0
   
 