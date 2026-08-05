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
                return [True,0]
            
            leftHeight = findHeight(root.left)
            rightHeight = findHeight(root.right)

            return[abs(leftHeight[1] - rightHeight[1]) <= 1 and leftHeight[0] and rightHeight[0], max(leftHeight[1],rightHeight[1])+1]
        
        return findHeight(root)[0]

            