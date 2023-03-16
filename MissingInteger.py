# Name : Anish Banswada
# Time Taken : 10 minutes

# Problem Description : Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

# Anticipated Strategy : One-directional running computation/total

# Assumptions -  size of input array is not 0, 

# Space Complexity - O(1)

# Time Complexity - O(nlogn)

# Function 
def MissingInteger(ar, size):
    size = size - 1
    if(ar[0] != 1):
        return 1
    if(ar[size-1] != (size+1)):
        return size+1
 
    a = 0
    b = size - 1
    mid = 0
    while b > a + 1:
        mid = (a + b) // 2
        if (ar[a] - a) != (ar[mid] - mid):
            b = mid
        elif (ar[b] - b) != (ar[mid] - mid):
            a = mid
    return ar[a] + 1

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
