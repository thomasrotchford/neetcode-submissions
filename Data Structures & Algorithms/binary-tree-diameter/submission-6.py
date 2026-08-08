# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root:TreeNode):

            if not root:
                return 0,0 

            lHeight = height(root.left)
            rHeight = height(root.right)
            diameter = max(lHeight[0]+rHeight[0],lHeight[1],rHeight[1])
            return max(lHeight[0],rHeight[0])+1, diameter


        return height(root)[1]
        

        