# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxd = 0

        s = [(root, 1)]
        while s:
            a, l = s.pop()
            if a.left:
                s.append((a.left, l+1))
            if a.right:
                s.append((a.right, l+1))
            maxd = max(l, maxd)
        
        return maxd