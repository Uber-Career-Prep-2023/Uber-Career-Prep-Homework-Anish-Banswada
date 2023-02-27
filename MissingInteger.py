# Name : Anish Banswada
# Time Taken : 10 minutes

# Problem Description : Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

# Anticipated Strategy : One-directional running computation/total

# Assumptions -  size of input array is not 0, 

# Space Complexity - O(1)

# Time Complexity - O(n)

# Function 
def MissingInteger(nums, k):
    i = 0
    while (i<len(nums)):
        if (i+1 != nums[i]):
            return i + 1
        i += 1
    return k

# Main

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 7]
    n = 7
    print("Expected 5 and got " + str(MissingInteger(arr,n)))
   
    arr = [1]
    n = 2
    print("Expected 2 and got " + str(MissingInteger(arr,n)))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    n = 12
    print("Expected 9 and got " + str(MissingInteger(arr,n)))
