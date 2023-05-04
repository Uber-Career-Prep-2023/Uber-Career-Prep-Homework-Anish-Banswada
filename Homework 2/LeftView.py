# Name : Anish Banswada
# Time Taken : 

# Problem Description : Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

# Anticipated Strategy : BFS

# Assumptions : 

# Space Complexity : O(n)

# Time Complexity : O(n)

# Function 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_view(root):
    if not root:
        return []

    queue = [root]
    left_view = []

    while queue:
        left_view.append(queue[0].val)

        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return left_view

# Main

if __name__ == "__main__":

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    assert left_view(root1) == [1, 2, 4]

    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(4)
    assert left_view(root2) == [1, 2, 3]


    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.right.right = TreeNode(5)
    assert left_view(root3) == [1, 2, 4]


    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.right.left = TreeNode(4)
    root4.right.right = TreeNode(5)
    assert left_view(root4) == [1, 2, 4]

    print('Testing completed')


    
    