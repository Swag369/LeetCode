# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
            
        ret = []
        q1 = [root]
        q2 = []

        dir = 0

        while q1 or q2:

            for i in q1:
                if i.left:
                    q2.append(i.left)
                if i.right:
                    q2.append(i.right)


            if dir % 2 == 0:
                ret.append(list(map(lambda x: x.val, q1)))
            else:
                ret.append(list(reversed(list(map(lambda x: x.val, q1)))))

            q1 = q2
            q2 = []


            dir += 1
        
        return ret