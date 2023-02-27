# Name : Anish Banswada

# Time Taken : 20 minutes

# Problem Description : Given an array of integers and a target integer, k, return the number of pairs of integers 
# in the array that sum to k. In each pair, the two items must be distinct elements (come from different indices in the array)

# Anticipated Strategy : One-directional running computation

# Assumptions -  Target can be positive or negative, 

# Function 
def twoSum(nums, target):
    vals = {}
    result = 0
    for index,value in enumerate(nums):
        remainder = target - value
        if remainder in vals:
            result += vals[remainder]
        vals[value] = vals.get(value, 0) + 1
    return result

# Main

if __name__ == "__main__":
    arr =  [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    k = 10
    print("Expected 3 and got " + str(twoSum(arr,k)))
    arr =  [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    k = -3
    print("Expected 1 and got " + str(twoSum(arr,k)))

    arr = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    k = 8
    print("Expected 3 and got " + str(twoSum(arr,k)))

    arr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    k = 5
    print("Expected 4 and got " + str(twoSum(arr,k)))

    arr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    k = 1
    print("Expected 0 and got " + str(twoSum(arr,k)))
   
 