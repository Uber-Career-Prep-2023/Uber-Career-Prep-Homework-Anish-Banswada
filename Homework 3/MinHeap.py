class heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def insert(self,element):
        self.arr.append(element)
        self.size += 1 
        current = self.size - 1
        parent = int((current - 1)/2)
        while parent >= 0 and self.arr[parent] > self.arr[current]:
            self.swap(parent,current)
            current = parent
            parent = int((current - 1)/2)
    
    def swap(self, parent, current):
        temp = self.arr[parent]
        self.arr[parent] = self.arr[current]
        self.arr[current] = temp

    
    def top(self):
        if self.size > 0:
            return self.arr[0]
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
        smallest = root
        if left_child < self.size and self.arr[root] > self.arr[left_child]:
            smallest = left_child
        if right_child < self.size and self.arr[smallest] > self.arr[right_child]:
            smallest = right_child
        if smallest != root:
            self.swap(root, smallest)
            self.heapify(smallest)
    
    def print_heap(self):
        print(self.arr)

if __name__ == "__main__":
    heap_1 = heap()
    heap_1.insert(1)
    heap_1.insert(3)
    heap_1.insert(5)
    heap_1.insert(2)
    assert heap_1.top() == 1
    heap_1.remove()
    assert heap_1.top() == 2
    heap_1.remove()
    assert heap_1.top() == 3
    heap_1.remove()
    assert heap_1.top() == 5

    heap_2 = heap()
    heap_2.insert(0)
    heap_2.insert(-2)
    heap_2.insert(-1)
    heap_2.insert(8)
    heap_2.insert(3)
    assert heap_2.top() == -2
    heap_2.remove()
    assert heap_2.top() == -1
    heap_2.remove()
    assert heap_2.top() == 0
    heap_2.remove()
    assert heap_2.top() == 3
    heap_2.remove()
    assert heap_2.top() == 8
    
    print("Testing completed")



    