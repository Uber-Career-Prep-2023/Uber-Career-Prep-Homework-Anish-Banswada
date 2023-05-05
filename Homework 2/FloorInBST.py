# Name : Anish Banswada
# Time Taken : 35 minutes

# Problem Description : Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.

# Anticipated Strategy :

# Assumptions : 

# Space Complexity : O(1)

# Time Complexity : (h)

# Function 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def floor_bst(root, target):
    floor_val = float('-inf')

    while root:
        if root.val == target:
            return root.val
        elif root.val < target:
            floor_val = root.val
            root = root.right
        else:
            root = root.left

    return floor_val


# Main

if __name__ == "__main__":

    root1 = TreeNode(8)
    root1.left = TreeNode(4)
    root1.right = TreeNode(12)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(6)
    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(14)
    assert floor_bst(root1, 5) == 4

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(9)
    assert floor_bst(root2, 1) == float('-inf')

    root3 = TreeNode(1)
    root3.right = TreeNode(2)
    assert floor_bst(root3, 3) == 2

   
    print("Testing completed")