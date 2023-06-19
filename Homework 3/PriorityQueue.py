class PriorityQueue:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def insert(self,element,weight):
        self.arr.append([element,weight])
        self.size += 1 
        current = self.size - 1
        parent = int((current - 1)/2)
        while parent >= 0 and self.arr[parent][1] < self.arr[current][1]:
            self.swap(parent,current)
            current = parent
            parent = int((current - 1)/2)
    
    def swap(self, parent, current):
        temp = self.arr[parent]
        self.arr[parent] = self.arr[current]
        self.arr[current] = temp

    
    def top(self):
        if self.size > 0:
            return self.arr[0][0]
        return None
    
    def remove(self):
        length = len(self.arr)
        if length <= 0:
            return None
        if length == 1:
            return self.arr.pop()
        self.arr[0]  = self.arr[length - 1]
        self.arr.pop()
        self.size -= 1
        return self.heapify(0)

    def heapify(self, root):
        left_child = 2 * root + 1
        right_child = 2 * root + 2
        largest = root
        if left_child < self.size and self.arr[root][1] < self.arr[left_child][1]:
            largest = left_child
        if right_child < self.size and self.arr[largest][1] < self.arr[right_child][1]:
            largest = right_child
        if largest != root:
            self.swap(root, largest)
            self.heapify(largest)
    
    def print_heap(self):
        print(self.arr)

if __name__ == "__main__":
    pq1 = PriorityQueue()
    pq1.insert('a',1)
    pq1.insert('b',3)
    pq1.insert('c',5)
    pq1.insert('d',2)
    assert pq1.top() == 'c'
    pq1.remove()
    assert pq1.top() == 'b'
    pq1.remove()
    assert pq1.top() == 'd'
    pq1.remove()
    assert pq1.top() == 'a'

    pq2 = PriorityQueue()
    pq2.insert(0,0)
    pq2.insert(-2,-2)
    pq2.insert(-1,-1)
    pq2.insert(8,8)
    pq2.insert(3,3)
    assert pq2.top() == 8
    pq2.remove()
    assert pq2.top() == 3
    pq2.remove()
    assert pq2.top() == 0
    pq2.remove()
    assert pq2.top() == -1
    pq2.remove()
    assert pq2.top() == -2
    
    print("Testing completed")



    