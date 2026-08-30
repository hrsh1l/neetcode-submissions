# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return None
            elif node ==p or node==q:
                return node

            leftValue = dfs(node.left)
            rightValue = dfs(node.right)

            if leftValue and rightValue:
                return node

            return leftValue if leftValue else rightValue
        
        return dfs(root)
        