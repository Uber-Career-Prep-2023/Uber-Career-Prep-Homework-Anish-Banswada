# Name : Anish Banswada
# Time Taken : 10 minutes

# Problem Description : Given a binary tree, determine if it is a binary search tree.

# Anticipated Strategy : Pre-order like traversal

# Assumptions : 

# Space Complexity :

# Time Complexity :
class Node:
    def __init__(self, data = None):
        self.val = data
        self.left = None
        self.right = None
# Function 
def IsBst(root):
    if not root:
        return True
    if root.left: 
        if root.left.val > root.val:
            return False
    if root.right:
        if root.right.val < root.val:
            return False
    return (IsBst(root.left) and IsBst(root.right))

# Main

if __name__ == "__main__":
    # Test case 1
    root = Node(4)
    assert IsBst(root) == True

    # Test case 2
    root = Node(4)
    root.left = Node(6)
    assert IsBst(root) == False

    # Test case 3
    root = Node(4)
    root.left = Node(2)
    assert IsBst(root) == True

    # Test case 4
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    assert IsBst(root) == True

    print("Testing completed")
   
 