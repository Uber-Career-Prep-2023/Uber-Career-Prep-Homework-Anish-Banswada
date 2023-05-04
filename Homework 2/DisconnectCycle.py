# Name : Anish Banswada
# Time Taken : 40 minutes

# Problem Description : Given a singly linked list, disconnect the cycle, if one exists.

# Anticipated Strategy : Fast-slow pointer

# Assumptions : 

# Space Complexity : O(1)

# Time Complexity : O(n)

# Function 
 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def disconnect_cycle(head: Node) -> None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return # No cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    fast = fast.next
    while fast.next != slow:
        fast = fast.next
    fast.next = None

if __name__ =="__main__":

    head1 = Node(10)
    head1.next = Node(18)
    head1.next.next = Node(12)
    head1.next.next.next = Node(9)
    head1.next.next.next.next = Node(11)
    head1.next.next.next.next.next = Node(4)
    head1.next.next.next.next.next.next = head1.next.next  
    disconnect_cycle(head1)
    assert head1.next.next.next.next.next.next is None  

    head2 = Node(10)
    head2.next = Node(18)
    head2.next.next = Node(12)
    head2.next.next.next = Node(9)
    head2.next.next.next.next = Node(11)
    head2.next.next.next.next.next = Node(4)
    disconnect_cycle(head2)
    assert head2.next.next.next.next.next.next is None 

    head3 = Node(10)
    head3.next = Node(18)
    head3.next.next = Node(12)
    head3.next.next.next = Node(9)
    head3.next.next.next.next = Node(11)
    head3.next.next.next.next.next = Node(4)
    head3.next.next.next.next.next.next = head3.next.next.next.next.next 
    disconnect_cycle(head3)
    assert head3.next.next.next.next.next.next is None  

    print("Testing completed")
