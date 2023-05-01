class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def insert_at_front(self, val):
        new_node = Node(val)
        new_node.prev = None
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else: 
            self.tail = new_node
        self.head = new_node

    def insert_at_back(self, val):
        new_node = Node(val)
        new_node.next = None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, loc, val):
        if not loc:
            return
        if self.tail == loc:
            return self.insert_at_back(loc,val)
        new_node = Node(val)
        new_node.next = loc.next
        loc.next = new_node
        new_node.next.prev = new_node
        new_node.prev = loc

    def delete_front(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        ptr = self.head.next
        self.head.next = None
        ptr.prev = None
        self.head = ptr

    def delete_back(self):
        if not self.head:
            return
        ptr = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        ptr.prev = None

    def delete_node(self, loc):
        if not self.head:
            return
        if self.head == loc:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            return
        previous = loc.prev
        post = loc.next
        previous.next = post
        post.prev = previous
        loc.next = None
        loc.prev = None

    def length(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        ptr = self.head
        s = ""
        while ptr:
            s += str(ptr.data) + " "
            ptr = ptr.next
        return(s[:-1])


if __name__ == "__main__":
        
    # Creating an instance of the linked list
    llist = LinkedList()

    # Inserting nodes at the front of the list
    llist.insert_at_front(1)
    assert llist.display() == ('1')

    llist.insert_at_front(2)
    assert llist.display() == ('2 1')

    llist.insert_at_front(3)
    assert llist.display() == ('3 2 1')

    # Inserting nodes at the back of the list
    llist.insert_at_back(4)
    assert llist.display() == ('3 2 1 4')

    llist.insert_at_back(5)
    assert llist.display() == ('3 2 1 4 5')

    # Inserting a node after a given node
    node = llist.head.next
    llist.insert_after(node, 6)
    assert llist.display() == ('3 2 6 1 4 5')

    # Deleting the front node
    llist.delete_front()
    assert llist.display() == ('2 6 1 4 5')

    # Deleting the last node
    llist.delete_back()
    assert llist.display() == ('2 6 1 4')

    # Deleting a specific node
    node_to_delete = llist.head.next
    llist.delete_node(node_to_delete)
    assert llist.display() == ('2 1 4')

    # Reversing the linked list
    #llist.reverse_iterative()
    #assert llist.display() == ('4 1 2')

    print("Testing completed successfully")