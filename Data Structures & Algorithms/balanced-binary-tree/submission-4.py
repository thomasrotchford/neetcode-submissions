# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def findHeight(root:TreeNode):

            if not root:
                return 0

            return max(findHeight(root.left),findHeight(root.right))+1

        if not root:
            return True
        
        if findHeight(root.left) == findHeight(root.right) or findHeight(root.left) == findHeight(root.right)+1 or findHeight(root.left)+1 == findHeight(root.right):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        