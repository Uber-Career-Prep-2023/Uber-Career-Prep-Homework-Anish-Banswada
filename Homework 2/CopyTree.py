# Name : Anish Banswada

# Time Taken : 30 minutes


# Problem Description : Given a binary tree, create a deep copy. Return the root of the new tree.

# Anticipated Strategy : Pre-order-like tree traversal

# Assumptions :  input is a non-empty binary tree

# Space Complexity : O(n)

# Time Complexity : O(n)

# Function 
class Node:
    def __init__(self, data = None):
        self.val = data
        self.left = None
        self.right = None

def CopyTree(root):
    if not root:
        return None
    new_node = Node(root.val)
    new_node.left = CopyTree(root.left)
    new_node.right = CopyTree(root.right)
    return new_node

# Main

if __name__ == "__main__":
    # Create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Create a deep copy of the binary tree
    new_root = CopyTree(root)

    # Verify that the original and new trees have the same structure and values
    assert root.val == new_root.val
    assert root.left.val == new_root.left.val
    assert root.right.val == new_root.right.val
    assert root.left.left.val == new_root.left.left.val
    assert root.left.right.val == new_root.left.right.val
    assert root.right.left.val == new_root.right.left.val
    assert root.right.right.val == new_root.right.right.val

    # Modify the original tree
    root.val = 10
    root.left.right.val = 20
    root.right.left.val = 30

    # Verify that the modified tree and the copy are different
    assert root.val != new_root.val
    assert root.left.right.val != new_root.left.right.val
    assert root.right.left.val != new_root.right.left.val

    print("Testing completed")

    
    