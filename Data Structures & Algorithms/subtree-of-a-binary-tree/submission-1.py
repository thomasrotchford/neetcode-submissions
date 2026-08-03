# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]):

            if root and subRoot:
                if root.val == subRoot.val:
                    return isSameTree(root.left, subRoot.left) and isSameTree(root.right,subRoot.right)
                else: 
                    return False

            elif not root and not subRoot:
                return True
            else:
                return False
       
        if not isSameTree(root,subRoot):
            if not root or not subRoot:
                return False
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else:
            return True





        
        