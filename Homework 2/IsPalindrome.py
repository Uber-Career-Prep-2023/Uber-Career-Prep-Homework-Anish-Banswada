# Name : Anish Banswada
# Time Taken : 

# Problem Description : Checks if a doubly linked list is a palindrom

# Anticipated Strategy : Catchup reset pointer

# Assumptions : 

# Space Complexity : O(1)

# Time Complexity : O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def is_palindrome(head):
    length = 0
    current = head
    prev_ = current
    while current is not None:
        prev_ = current
        length += 1
        current = current.next
    if length < 2:
        return True
    left = head
    right = prev_
    
    for i in range(length // 2):
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True

if __name__== "__main__":
    head = Node(1)
    assert is_palindrome(head) == True

    head = Node(1)
    head.next = Node(1)
    head.next.prev = head
    assert is_palindrome(head) == True

    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    assert is_palindrome(head) == False

    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(1)
    head.next.next.prev = head.next
    assert is_palindrome(head) == True

    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    assert is_palindrome(head) == False

    print('Testing completed')