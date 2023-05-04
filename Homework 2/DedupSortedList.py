# Using the linkedlist implementation from the previous problem
class Node:
    def __init__(self, val = None):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_back(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
    
    def display(self):
        ptr = self.head
        s = ""
        while ptr:
            s += str(ptr.data) + " "
            ptr = ptr.next
        return(s[:-1])

# Name : Anish Banswada
# Time Taken : 20 minutes for implementation 

# Problem Description : Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

# Anticipated Strategy : Linked list reset/catch-up two-pointer

# Assumptions : 

# Space Complexity : O(1)

# Time Complexity : O(n)

# Function

def DedupSortedList(linked_list):
    prev = linked_list.head
    curr = linked_list.head
    if not curr:
        return None
    while curr is not None:
        while curr is not None and curr.data == prev.data:
            curr = curr.next
        prev.next = curr
        prev = curr 

# Main 

if __name__ == '__main__':
    list1 = LinkedList()
    list1.insert_at_back(1)
    list1.insert_at_back(2)
    list1.insert_at_back(2)
    list1.insert_at_back(4)
    list1.insert_at_back(5)
    list1.insert_at_back(5)
    list1.insert_at_back(5)
    list1.insert_at_back(10)
    list1.insert_at_back(10)

    DedupSortedList(list1)

    assert list1.display() == "1 2 4 5 10"

    list2 = LinkedList()
    list2.insert_at_back(8)
    list2.insert_at_back(8)
    list2.insert_at_back(8)
    list2.insert_at_back(8)

    DedupSortedList(list2)

    assert list2.display() == "8"

    list3 = LinkedList()
    list3.insert_at_back(8)
    list3.insert_at_back(8)
    list3.insert_at_back(8)
    list3.insert_at_back(8)

    list3.insert_at_back(9)
    list3.insert_at_back(9)
    list3.insert_at_back(9)
    list3.insert_at_back(9)

    list3.insert_at_back(19)
    list3.insert_at_back(19)
    list3.insert_at_back(19)
    list3.insert_at_back(19)


    DedupSortedList(list3)

    assert list3.display() == "8 9 19"

    print("Testing Completed")