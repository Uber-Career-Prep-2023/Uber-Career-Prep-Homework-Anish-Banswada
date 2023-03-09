# Name : Anish Banswada
# Time Taken : 30 minutes

# Problem Description : Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once.

# Anticipated Strategy : Reset/Catchup Pointer

# Assumptions -  

# Space Complexity - O(1)

# Time Complexity - O(n)

# Function 

def DedupArray(lst):
    d_num = lst[0]
    d_ind = 1
    for index, number in enumerate(lst):
        if (number != d_num):
            lst[d_ind] = number
            d_ind += 1
            d_num = number
    return lst[:d_ind]


# Main

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print("Expected [1, 2, 3, 4] and got " +  str(DedupArray(arr)))
   
    arr = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
    print("Expected [0, 1, 4, 5, 8, 9, 10, 11, 15] and got " +  str(DedupArray(arr)))
 
    arr = [1, 3, 4, 8, 10, 12]
    print("Expected [1, 3, 4, 8, 10, 12] and got " +  str(DedupArray(arr)))

    arr = [1, 1,1,1]
    print("Expected [1] and got " +  str(DedupArray(arr)))
    