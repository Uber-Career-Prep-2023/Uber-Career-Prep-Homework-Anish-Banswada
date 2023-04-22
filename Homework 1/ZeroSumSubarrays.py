# Name : Anish Banswada
# Time Taken : 50 mins

# Problem Description : Given an array of integers, count the number of subarrays that sum to zero.

# Anticipated Strategy : Hashing

# Assumptions - 

# Time Complexity - O(n)

# Space Complexity - O(n)

# Function 

def zero(nums):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums,0)
        d[sums] = d.get(sums,0) + 1
        
    return(count)

# Main

if __name__ == "__main__":
    arr = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    print("Expected 2 and got " + str(zero(arr)))
   

 