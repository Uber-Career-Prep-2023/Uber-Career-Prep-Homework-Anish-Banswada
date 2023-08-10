# Name : Anish Banswada

# Strategy : Tabulation 

# Time Taken : 15 minutes

# Assumptions : None

# Space Complexity : O(n)

# Time Complexity : O(n)

# Function 
import math
def catalanNums(n):
    res = [math.factorial(2*i)/(math.factorial(i+1)*math.factorial(i)) for i in range(n+1)]
    return res

def newCatalanNums(n):  # was not able to figure out the dp solution until i looked at the relation  res[i] += res[j] + res[i-j-1]
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    res = [0] * (n+1)
    res[0] = 1
    res[1] = 1
    for i in range(2,n+1):
        for j in range(i):
            res[i] += res[j] * res[i-j-1]
    return res

# Main

if __name__ == "__main__":
    assert catalanNums(5) == [1, 1, 2, 5, 14, 42]
    assert newCatalanNums(5) == [1, 1, 2, 5, 14, 42]
    assert catalanNums(1) == [1,1]
    assert newCatalanNums(1) == [1,1]
    print("Testing completed")
   
 