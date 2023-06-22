# Name : Anish Banswada

# Time Taken : 40 minutes

# Assumptions : None

# Space Complexity : O(1)

# Time Complexity : O(height of grid * breadth of grid)

# Function 
def numIslands(grid):
    count = 0
    for i in range (len(grid)):
        for j in range (len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count
    
def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = 0
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

# Main

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    assert numIslands(grid) == 1
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    assert numIslands(grid) == 3
    grid = [["1", "0", "1"],["1", "0", "1"]]
    assert numIslands(grid) == 2
    print("Testing completed")
   
 