class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            # no duplicates allowed
            pass

    def contains(self, val):
        return self._contains(val, self.root)

    def _contains(self, val, current_node):
        if current_node is None:
            return False
        elif val == current_node.data:
            return True
        elif val < current_node.data:
            return self._contains(val, current_node.left)
        else:
            return self._contains(val, current_node.right)

    def min(self):
        if self.root is None:
            return None
        else:
            current_node = self.root
            while current_node.left is not None:
                current_node = current_node.left
            return current_node.data

    def max(self):
        if self.root is None:
            return None
        else:
            current_node = self.root
            while current_node.right is not None:
                current_node = current_node.right
            return current_node.data

    def delete(self, val):
        if self.root is None:
            return None
        else:
            return self._delete(val, self.root)

    def _delete(self, val, current_node):
        if current_node is None:
            return current_node
        elif val < current_node.data:
            current_node.left = self._delete(val, current_node.left)
        elif val > current_node.data:
            current_node.right = self._delete(val, current_node.right)
        else:
            if current_node.left is None:
                temp_node = current_node.right
                current_node = None
                return temp_node
            elif current_node.right is None:
                temp_node = current_node.left
                current_node = None
                return temp_node
            else:
                temp_node = self._find_min_node(current_node.right)
                current_node.data = temp_node.data
                current_node.right = self._delete(temp_node.data, current_node.right)
        return current_node

    def _find_min_node(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

if __name__ == "__main__":

    # Create a new BST object
    bst = BinarySearchTree()

    # Insert some nodes
    bst.insert(5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(8)

    # Test contains method
    assert bst.contains(5) == True
    assert bst.contains(2) == True
    assert bst.contains(7) == True
    assert bst.contains(1) == True
    assert bst.contains(3) == True
    assert bst.contains(6) == True
    assert bst.contains(8) == True
    assert bst.contains(0) == False
    assert bst.contains(4) == False
    assert bst.contains(9) == False

    # Test min method
    assert bst.min() == 1

    # Test max method
    assert bst.max() == 8

    # Test delete method
    bst.delete(7)
    assert bst.contains(7) == False
    assert bst.max() == 8

    bst.delete(5)
    assert bst.contains(5) == False
    assert bst.max() == 8

    bst.delete(1)
    assert bst.contains(1) == False
    assert bst.min() == 2

    bst.delete(2)
    assert bst.contains(2) == False
    assert bst.min() == 3

    bst.delete(8)
    assert bst.contains(8) == False
    assert bst.max() == 6

    print("Testing successfully completed")
