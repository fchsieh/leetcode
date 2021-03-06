# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def build_graph(self, root):
        if not root:
            return
        if root.left:
            self.graph[root.val].add(root.left.val)
            self.graph[root.left.val].add(root.val)
            self.build_graph(root.left)
        if root.right:
            self.graph[root.val].add(root.right.val)
            self.graph[root.right.val].add(root.val)
            self.build_graph(root.right)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.build_graph(root)
        res = [target.val]
        seen = set([])
        
        for _ in range(k):
            size, next_level = len(res), []
            for _ in range(size):
                cur = res.pop()
                if cur not in seen:
                    next_level.extend(list(self.graph[cur]))
                    seen.add(cur)
            res = set(next_level)
        return [val for val in res if val not in seen]
        