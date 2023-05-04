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
# Time Taken : 30 minutes 

# Problem Description : Given a singly linked list, move the nth from the last element to the front of the list.

# Anticipated Strategy : Linked list reset/catch-up two-pointer

# Assumptions : 

# Space Complexity : O(1)

# Time Complexity : O(n)

# Function 
def MoveLastToFirst (linked_list, k):
    ptr = linked_list.head
    count = 0
    while ptr:
        ptr = ptr.next
        count += 1
    if count <= k:
        return None
    target_pos = count - k 
    tracker = 0
    curr = linked_list.head
    prev = curr
    while tracker < target_pos:
        prev = curr
        tracker += 1
        curr = curr.next
    new_node = Node(curr.data)
    new_node.next = linked_list.head
    linked_list.head = new_node
    prev.next = curr.next
    
    
# Main

if __name__ == "__main__":

    ll = LinkedList()
    ll.insert_at_back(15)
    ll.insert_at_back(2)
    ll.insert_at_back(8)
    ll.insert_at_back(7)
    ll.insert_at_back(20)
    ll.insert_at_back(9)
    ll.insert_at_back(11)
    ll.insert_at_back(6)
    ll.insert_at_back(19)
    MoveLastToFirst(ll, 2)
    assert ll.display() == "6 15 2 8 7 20 9 11 19"

 
    ll = LinkedList()
    ll.insert_at_back(1)
    ll.insert_at_back(2)
    ll.insert_at_back(3)
    ll.insert_at_back(4)
    ll.insert_at_back(5)
    MoveLastToFirst(ll, 3)
    assert ll.display() == "3 1 2 4 5"


    ll = LinkedList()
    ll.insert_at_back(1)
    ll.insert_at_back(2)
    ll.insert_at_back(3)
    ll.insert_at_back(4)
    ll.insert_at_back(5)
    MoveLastToFirst(ll, 5)
    assert ll.display() == "1 2 3 4 5"


    ll = LinkedList()
    ll.insert_at_back(1)
    MoveLastToFirst(ll, 1)
    assert ll.display() == "1"

    print("Testing completed")
