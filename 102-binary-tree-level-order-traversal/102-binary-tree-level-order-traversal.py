# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        level = 0
        
        def bfs(node, level):
            if not node:
                return
            if level >= len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)
            
            bfs(node.left, level+1)
            bfs(node.right, level+1)
        
        bfs(root, 0)
        return res