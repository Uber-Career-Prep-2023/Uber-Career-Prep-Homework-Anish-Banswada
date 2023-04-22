# Name : Anish Banswada
# Time Taken : 50 minutes

# Problem Description : Given a list of integer pairs representing the 
# low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

# Anticipated Strategy - Two pointers 

# Assumptions -  Intervals in the input are in the form of list of lists

# Space Complexity - O(n)

# Time Complexity - O(nlogn)

# Function 

def MergeIntervals(lst):
    res = []
    for item in sorted(lst, key = lambda x: x[0]):
        if res and item[0] <= res[-1][1]:
            res[-1][1] = max(item[1], res[-1][1])
        else:
            res.append(item)
    return res    

# Main

if __name__ == "__main__":
    Input = [[2, 3], [4, 8], [1, 2], [5, 7], [9, 12]]
    print("Expected [(4, 8), (1, 3), (9, 12)] and got " + str(MergeIntervals(Input)))

    Input = [[5, 8], [6, 10], [2, 4], [3, 6]]
    print("Expected [(2, 10)] and got " + str(MergeIntervals(Input)))

    Input = [[10, 12], [5, 6], [7, 9], [1, 3]]
    print("Expected [(10, 12), (5, 6), (7, 9), (1, 3)] and got " + str(MergeIntervals(Input)))

   
 