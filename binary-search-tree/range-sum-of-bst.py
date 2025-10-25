# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        a = 0
        if not root:
            return 0
        if root.val >= low and root.val <= high:
            a = root.val
        return a + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)