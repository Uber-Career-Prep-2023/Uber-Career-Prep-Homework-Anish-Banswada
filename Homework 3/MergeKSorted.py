# Name : Anish Banswada

# Time Taken : 

# Assumptions : 

# Space Complexity : O(k*n)

# Time Complexity : O(k log n)
import heapq
# Function 
def merge(k, lists):
    temp = []
    res = []
    for sub_list in lists:
        for item in sub_list:
            heapq.heappush(temp, item)
    while temp:
        res.append(heapq.heappop(temp))
    return res
        


# Main

if __name__ == "__main__":
    assert merge(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
    assert merge(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]) == [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
    assert merge(4, [[1,2],[-1,-2], [3,-5],[6,7]]) == [-5,-2,-1,1,2,3,6,7]
    print("Testing completed")
 