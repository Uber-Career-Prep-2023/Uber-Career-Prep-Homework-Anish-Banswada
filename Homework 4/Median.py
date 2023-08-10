# Name : Anish Banswada

# Strategy : Maintain 2 heaps

# Time Taken :  30 minutes

# Assumptions : None

# Space Complexity : O(n)

# Time Complexity : O(log n) for insert, O(1) for median
import heapq
# Function 
class findMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def insert(self,num):
        heapq.heappush(self.max_heap,-num)
        heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        
    def median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2.0
# Main

if __name__ == "__main__":
    medianFinder = findMedian()
    medianFinder.insert(1)
    medianFinder.insert(2)
    assert medianFinder.median() == 1.5
    medianFinder.insert(3)
    assert medianFinder.median() == 2.0
    print('Testing completed')
   
 