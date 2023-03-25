# Name : Anish Banswadas
# Time Taken : 40 minutes

# Problem Description : Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

# Anticipated Strategy : fixed size sliding window

# Assumptions -  Non-empty array, k > 0

# Time Complexity - O(n)

# Space Complexity -  O(1)

# Function 
def MaxMeanSubArray(nums, k):
    if len(nums) == 1:
        return nums[0]
    running_sum = 0
    max_sum = float('-inf')
    window_start = 0
    for window_end in range(0,len(nums)):
        running_sum += nums[window_end]
        if(window_end >= k - 1):
            max_sum = max(running_sum, max_sum)
            running_sum -= nums[window_start]
            window_start += 1
    return float(max_sum)/k

# Main

if __name__ == "__main__":
    input =  [4, 5, -3, 2, 6, 1]
    k = 2
    print("Result = ", MaxMeanSubArray(input, k), " and expected = 4.5")


    input =  [4, 5, -3, 2, 6, 1]
    k = 3
    print("Result = ", MaxMeanSubArray(input, k), " and expected = 3")

    input =  [1, 1, 1, 1, -1, -1, 2, -1, -1]
    k = 5
    print("Result = ", MaxMeanSubArray(input, k), " and expected = 1")
 