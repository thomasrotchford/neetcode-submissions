class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        

        rowLen = len(matrix[0])
        colLen = len(matrix)

        l=0
        r=(rowLen*colLen)-1

        while l<=r:
            #calc midpt using l->r coords
            m = ((r-l)//2)+l
            
            #check value of midpt using r,c coords
            midpt = matrix[m//rowLen][m%rowLen]
            
            if midpt < target:
                l = m+1
            elif midpt > target:
                r = m-1
            else:
                return True

        return False
        