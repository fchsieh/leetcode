# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            l = height(node.left) + 1
            r = height(node.right) + 1
            
            return max(l, r)
        
        if not root:
            return True
        
        return abs(height(root.left) - height(root.right)) <= 1 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)