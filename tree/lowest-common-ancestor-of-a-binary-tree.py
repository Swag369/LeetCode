# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path = []
        p_path = 1
        q_path = 2

        def dfs(node):

            nonlocal p_path, q_path

            path.append(node)

            # print("node, path", node.val, list(map(lambda x: x.val, path)))

            if p_path != 1 and q_path != 2:
                return

            if node.val == p.val:
                p_path = list(path)
                # print("saved", list(map(lambda x: x.val, p_path)))
            elif node.val == q.val:
                q_path = list(path)
                # print("saved", list(map(lambda x: x.val, q_path)))
            
            if node.right is not None:
                dfs(node.right)
            if node.left is not None:
                dfs(node.left)

            path.pop()
            


        dfs(root)
        # print(list(map(lambda x: x.val, p_path)))
        # print(list(map(lambda x: x.val, q_path)))

        for i in range(min(len(q_path), len(p_path))):
            # print(i)
            if q_path[i] != p_path[i]:
                # print(q_path[i-1].val)
                return q_path[i-1]
            if i == min(len(q_path), len(p_path))-1:
                # print(q_path[i].val)
                return q_path[i]