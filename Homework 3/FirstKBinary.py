# Name : Anish Banswada

# Time Taken : 40 minutes

# Assumptions : None

# Space Complexity : O(n)

# Time Complexity : O(n)

# Function 

from collections import deque

def FirstKBinary(k):
    if (k <= 0):
        return []
    res = ['0']
    queue = deque()
    queue.append('1')
    for i in range(k):
        cur = queue.popleft()
        res.append(cur)
        queue.append(cur + '0')
        queue.append(cur + '1')

    return res[:-1]

# Main

if __name__ == "__main__":
    assert FirstKBinary(1) == ["0"]
    assert FirstKBinary(3) == ["0", "1", "10",]
    assert FirstKBinary(5) == ["0", "1", "10", "11", "100"]
    assert FirstKBinary(10) == ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
    assert FirstKBinary(-1) == []
    print("Testing completed")