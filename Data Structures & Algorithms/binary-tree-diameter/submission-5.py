# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #after successful sub, got code reviewed to elim unecessary case
    #help used: topics, reccomended time and space, ai code review
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root:TreeNode):#->(height,diameter)
            
            #subtree has a parent but is null
            if not root:
                return 0, 0

            left = dfs(root.left)
            
            right = dfs(root.right)
            
            #edges=nodes-1
            #if one tree exists, it is the diameter of that tree if it has a diameter
            #if both exist, it is the sum of heights of those trees
            diameter = max(left[0]+right[0],left[1],right[1])


            #print(root.val)
            #print(" left: ", left[0],left[1])
            #print("right: ", right[0],right[1])   
             
            return max(left[0],right[0])+1, diameter

        #sol = dfs(root)
        #print(sol)
        return dfs(root)[1]

        
        